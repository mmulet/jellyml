import { Donut } from "./Donut";
import { state_to_position } from "./DonutState";
import { find_next_donut } from "./find_next_donut";
import { RectPosition } from "./RectPosition";

export interface UFO {
  x: number;
  y: number;
  time: number;
  left: boolean;
  clockwise: boolean;
  donut: Donut | null;
  abducting_time: number;
  wait_time: number;
  abducting_state: "waiting" | "wait_for_abduct" | "abducting";
}

export interface UpdateInput {
  ufos: UFO[];
  main_position: RectPosition;
  donuts: Donut[];
}

export const update_ufos = (
  { ufos, main_position, donuts }: UpdateInput,
  timeDifference: number
) => {
  for (const ufo of ufos) {
    ufo.time += timeDifference;
    ufo.y = main_position.bottom - 100;
    ufo.x = ufo.left ? main_position.left - 16 : main_position.right - 16;
    switch (ufo.abducting_state) {
      case "waiting":
        const next_donut = find_next_donut({
          donut_holder: ufo,
          main_position,
          donuts,
          animation_length: 0.2,
          time_threshold: 0.3,
          pure_only: false,
        });
        if (next_donut) {
          continue;
        }
        ufo.abducting_state = "wait_for_abduct";
      /**
       * Fallthrough on purpose
       */
      case "wait_for_abduct":
        ufo.donut!.y += ufo.donut!.vy * timeDifference;
        ufo.wait_time += timeDifference;
        if (ufo.wait_time > 0.4) {
          ufo.abducting_time += timeDifference;
        }
        if (ufo.wait_time < 1.1) {
          continue;
        }
        ufo.abducting_state = "abducting";
      /**
       * Fallthrough on purpose
       */
      case "abducting":
        ufo.abducting_time += timeDifference;
        if (ufo.abducting_time < 1.94) {
          continue;
        }
        ufo.abducting_state = "waiting";
        ufo.wait_time = 0;
        ufo.abducting_time = 0;
        ufo.donut = null;
        return;
    }
  }
};

export interface DrawInput {
  context: CanvasRenderingContext2D;
  sprites: HTMLImageElement;
  ufos: UFO[];
}

export const draw_ufos = (input: DrawInput) => {
  const { context, sprites, ufos } = input;
  for (const ufo of ufos) {
    if (ufo.donut) {
      draw_ufo_donut(input, ufo);
    }

    {
      const frame = Math.floor(ufo.abducting_time * 15) % 30;
      const sx = 256 + 32 * (frame % 8);
      const sy = 64 * 3 + 64 * Math.floor(frame / 8);
      context.drawImage(
        sprites,
        sx,
        sy,
        32,
        64,
        ufo.x + 16,
        ufo.y + 45,
        32,
        64
      );
    }

    const raw_frame = Math.floor(ufo.time * 10) % 19;
    const frame = ufo.clockwise ? raw_frame : 18 - raw_frame;
    const sx = 64 * (frame % 4);
    const sy = 128 + 64 * Math.floor(frame / 4);
    context.drawImage(sprites, sx, sy, 64, 64, ufo.x, ufo.y, 64, 64);
  }
};

const donut_abduct_animation = {
  22: { x: 4, y: -20, size: 24 },
  23: { x: 8, y: -25.6, size: 16 },
  24: { x: 10, y: -29.85, size: 12 },
  25: { x: 10, y: -32.45, size: 12 },
  26: { x: 12, y: -38.25, size: 8 },
  27: { x: 12, y: -44.25, size: 8 },
  28: { x: 14, y: -53.84, size: 4 },
  29: { x: 14, y: -62.8, size: 4 },
};

const get_abduct_animation_offsets = (ufo: UFO) => {
  const default_offset = { x: 0, y: 0, size: 32 };
  if (ufo.abducting_state !== "abducting") {
    return default_offset;
  }
  const frame = Math.floor(ufo.abducting_time * 15) % 30;
  return donut_abduct_animation[frame] ?? default_offset;
};

const draw_ufo_donut = ({ context, sprites }: DrawInput, ufo: UFO) => {
  const donut = ufo.donut!;
  /**
   * same as draw_donut
   */
  const { x, y } = state_to_position(donut.state);
  const { x: x_o, y: y_o, size } = get_abduct_animation_offsets(ufo);

  context.drawImage(
    sprites,
    x,
    y,
    32,
    32,
    donut.x + x_o + ufo.x,
    donut.y + y_o + ufo.y,
    size,
    size
  );
};
