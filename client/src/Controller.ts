import { Donut } from "./Donut";
import { not_eaten } from "./DonutState";
import { draw_donut } from "./draw_donut";
import { makeAnimationCanvas } from "./makeAnimationCanvas";
import { MouseOrTouchInput } from "./MouseOrTouchInput";
import { setupMouseAndTouchListeners } from "./setupMouseAndTouchListeners";
import { Touches } from "./Touches";
import { handle_collisions } from "./handle_collisions";
import {
  DonutMaker,
  draw_donut_maker,
  update_donut_makers,
} from "./DonutMaker";
import {
  draw_jelly_sprite,
  JellySprite,
  update_jelly_sprites,
} from "./JellySprite";
import { draw_tentacle, Tentacle, update_tentacle } from "./Tentacle";
import { RectPosition } from "./RectPosition";
import { load_image } from "./load_image";
import { draw_ufos, UFO, update_ufos } from "./UFO";

export class Controller {
  width: number;
  height: number;
  context: CanvasRenderingContext2D;

  touches: Touches = new Map<number, MouseOrTouchInput>();
  mouse: MouseOrTouchInput | null = null;

  lastFrameTime: number | null = null;
  timeSinceLastAnimationFrame: number = 0;

  donut_makers: DonutMaker[] = [
    {
      x: 0,
      y: -32,
      left: true,
      time: 0,
      state: "open",
      just_opened: false,
    },
    {
      x: 0,
      y: -32,
      left: false,
      time: -1,
      state: "open",
      just_opened: false,
    },
  ];

  ufos: UFO[] = [
    {
      x: 0,
      y: 0,
      time: 0,
      left: true,
      clockwise: true,
      donut: null,
      abducting_time: 0,
      abducting_state: "waiting",
      wait_time: 0,
    },
    {
      x: 0,
      y: 0,
      time: 0,
      left: false,
      clockwise: false,
      donut: null,
      abducting_time: 0,
      abducting_state: "waiting",
      wait_time: 0,
    },
    {
      x: 0,
      y: 0,
      time: 0,
      left: true,
      clockwise: true,
      donut: null,
      abducting_time: 0,
      abducting_state: "waiting",
      wait_time: 0,
    },
    {
      x: 0,
      y: 0,
      time: 0,
      left: false,
      clockwise: false,
      donut: null,
      abducting_time: 0,
      abducting_state: "waiting",
      wait_time: 0,
    },
  ];

  jelly_sprites: JellySprite[] = [];

  tentacle: Tentacle = {
    x: 0,
    y: 0,
    left: true,
    state: "wait_for_scroll",
    time: 0,
    wait_time: 0,
    wait_forward: true,
    wait_count: 0,

    donut_find_time: 0,
    donut: null,
  };

  main = document.getElementById("main")!;

  animation_toggle = document.getElementById(
    "animation-toggle"
  )! as HTMLInputElement;

  animation_disabled = false;

  main_position: RectPosition = {
    left: 0,
    top: 0,
    right: 0,
    bottom: 0,
  };

  donuts: Donut[] = [];

  sprites = load_image("/static/sprites.png");

  tentacle_image = load_image("/static/tentacle.png");
  disappointed_tentacle_image = load_image("/static/tentacle_disappointed.png");

  tentacle_line = document.getElementById("tentacle-line")!;
  original_transform: DOMMatrix;

  constructor() {
    const ratio = window.devicePixelRatio || 1;
    const longest_side = Math.max(screen.width, screen.height);
    this.width = longest_side;
    this.height = longest_side;

    const maybeContext = makeAnimationCanvas(this.width, this.height, ratio);
    if (!maybeContext) {
      throw new Error("Could not make Animation canvas");
    }
    this.context = maybeContext.context;
    this.context.imageSmoothingEnabled = false;
    this.context.fillStyle = "white";

    setupMouseAndTouchListeners({
      touches: this.touches,
      get_mouse: () => this.mouse,
      set_mouse: (mouse: MouseOrTouchInput | null) => (this.mouse = mouse),
    });
    this.animation_toggle.addEventListener("change", ({ target }) => {
      this.animation_disabled = !(target as HTMLInputElement).checked;
      if (this.animation_disabled) {
        return;
      }
      this.lastFrameTime = null;
      requestAnimationFrame(this.updateStateAndDraw);
    });
    this.original_transform = this.context.getTransform();

    requestAnimationFrame(this.updateStateAndDraw);
  }
  updateStateAndDraw = (totalTimeElapsed: number) => {
    if (this.animation_disabled) {
      this.context.clearRect(0, 0, this.width, this.height);
      return;
    }

    this.updateState(totalTimeElapsed);
    this.draw();

    requestAnimationFrame(this.updateStateAndDraw);
  };

  updateState = (totalTimeElapsed: number) => {
    const timeDifference =
      this.lastFrameTime == null ? 0 : totalTimeElapsed - this.lastFrameTime;
    this.lastFrameTime = totalTimeElapsed;
    const timeIncrement = timeDifference / 1000;

    this.timeSinceLastAnimationFrame += timeIncrement;

    const main_client_rect = this.main.getBoundingClientRect();
    this.main_position = {
      left: main_client_rect.left,
      top: main_client_rect.top,
      right: main_client_rect.right - 32,
      bottom: main_client_rect.bottom - 32,
    };

    handle_collisions(this);

    for (const donut of this.donuts) {
      donut.y += timeIncrement * donut.vy;
    }
    update_donut_makers(this.donut_makers, timeIncrement, this.spawn_donut);
    update_jelly_sprites(this.jelly_sprites, timeIncrement);
    update_tentacle(this, timeIncrement);
    update_ufos(this, timeIncrement);
    /**
     * Touch and requestAnimationFrame may not be
     * updated in sync. Make sure the difference is only
     * applied once, by deleting it now.
     */
    for (const [_, touch] of this.touches) {
      touch.difference = null;
    }
    if (this.mouse) {
      this.mouse.difference = null;
    }
  };

  spawn_donut = (maker: DonutMaker) => {
    const donut: Donut = {
      x: maker.x,
      y: maker.y + 32,
      vy: 100,
      state: {
        top: not_eaten,
        right: not_eaten,
        left: not_eaten,
        bottom: not_eaten,
      },
      left: maker.left,
    };
    this.donuts.push(donut);
  };

  draw_side = (left: boolean) => {
    for (const jelly_sprite of this.jelly_sprites) {
      if (jelly_sprite.left != left) {
        continue;
      }
      draw_jelly_sprite(this.context, this.sprites, jelly_sprite);
    }

    for (const maker of this.donut_makers) {
      if (maker.left != left) {
        continue;
      }
      draw_donut_maker(this.context, this.sprites, maker);
    }

    for (const donut of this.donuts) {
      if (donut.left != left) {
        continue;
      }
      draw_donut(this.context, this.sprites, donut);
    }
  };

  adjust_context_for_viewport = () => {
    const view_port = window.visualViewport;
    if (!view_port) {
      return;
    }
    this.context.translate(view_port.offsetLeft, view_port.offsetTop);
  };

  draw = () => {
    this.context.setTransform(this.original_transform);
    this.context.clearRect(0, 0, this.width, this.height);

    this.adjust_context_for_viewport();

    const left_position = {
      x: this.main_position.left,
      y: this.main_position.top,
    };
    const right_position = {
      x: this.main_position.right,
      y: this.main_position.top,
    };

    this.context.translate(left_position.x, left_position.y);
    this.draw_side(true);
    this.context.translate(
      -left_position.x + right_position.x,
      -left_position.y + right_position.y
    );
    this.draw_side(false);
    this.context.translate(-right_position.x, -right_position.y);
    draw_tentacle(this);
    draw_ufos(this);
  };
}
