import { Donut } from "./Donut";
import { RectPosition } from "./RectPosition";
import { find_next_donut } from "./find_next_donut";
import { animate_tentacles_grabbed_donut } from "./animate_tentacles_grabbed_donut";
import { draw_tentacle_donut } from "./draw_tentacle_donut";
export interface Tentacle {
  x: number;
  y: number;
  left: true;

  time: number;

  wait_time: number;
  wait_forward: boolean;
  wait_count: number;

  donut_find_time: number;

  donut: Donut | null;
  state:
    | "wait_for_scroll"
    | "animating_1"
    | "wait_for_donut"
    | "wait_for_donut_timing"
    | "animating_2"
    | "grabbing_donut"
    | "finished"
    | "disappointed";
}

export interface UpdateInput {
  tentacle: Tentacle;
  main_position: RectPosition;
  donuts: Donut[];
  tentacle_line: HTMLElement;
}

export const update_tentacle = (input: UpdateInput, timeIncrement: number) => {
  const { tentacle, main_position, donuts, tentacle_line } = input;
  if (tentacle.state === "finished") {
    return;
  }
  const line = tentacle_line.getBoundingClientRect();
  tentacle.x = main_position.left;
  tentacle.y = line.bottom;
  switch (tentacle.state) {
    case "wait_for_scroll":
      if (line.top > 400) {
        return;
      }
      tentacle.state = "animating_1";
    /**Fallthrough on purpose */
    case "animating_1":
      tentacle.time += timeIncrement;
      if (tentacle.time < 4) {
        return;
      }
      tentacle.state = "wait_for_donut";
      tentacle.wait_time = tentacle.time;
    /**Fallthrough on purpose */
    case "wait_for_donut":
      const next_donut = find_next_donut({
        donut_holder: tentacle,
        main_position,
        donuts,
        animation_length: 0.7,
        time_threshold: 0.8,
        pure_only: true,
      });
      if (next_donut) {
        update_wait_time(tentacle, timeIncrement);
        return;
      }
      tentacle.state = "wait_for_donut_timing";
    /**Fallthrough on purpose */
    case "wait_for_donut_timing":
      tentacle.donut!.y += tentacle.donut!.vy * timeIncrement;
      tentacle.donut_find_time += timeIncrement;
      if (tentacle.donut!.y + tentacle.donut!.vy * 0.7 < 0) {
        update_wait_time(tentacle, timeIncrement);
        return;
      }
      tentacle.state = "animating_2";
    /**Fallthrough on purpose */
    case "animating_2":
      tentacle.donut!.y += tentacle.donut!.vy * timeIncrement;
      if (tentacle.time < 4.8) {
        tentacle.time += timeIncrement;

        return;
      }
      tentacle.state = "grabbing_donut";
    /**Fallthrough on purpose */
    case "grabbing_donut":
      tentacle.time += timeIncrement;
      animate_tentacles_grabbed_donut(tentacle);
      if (tentacle.time < 10) {
        return;
      }
      tentacle.state = "finished";
      return;
    case "disappointed":
      tentacle.time += timeIncrement;
      if (tentacle.time < 5.07) {
        return;
      }
      tentacle.state = "finished";
      return;
  }
};

export interface DrawInput {
  context: CanvasRenderingContext2D;
  tentacle_image: HTMLImageElement;
  tentacle: Tentacle;
  sprites: HTMLImageElement;
  tentacle_line: HTMLElement;
  disappointed_tentacle_image: HTMLImageElement;
}

export const draw_tentacle = (input: DrawInput) => {
  const { context, tentacle, sprites, tentacle_image, tentacle_line } = input;
  if (tentacle.state === "finished") {
    return;
  }
  if (tentacle.state === "disappointed") {
    draw_disappointed_state(input);
    return;
  }
  const frame = Math.min(
    127,
    Math.floor(get_tentacle_frame_time(tentacle) * 15)
  );

  const sx = (frame % 8) * 128;
  const sy = Math.floor(frame / 8) * 64;

  context.drawImage(
    tentacle_image,
    sx,
    sy,
    128,
    64,
    tentacle.x,
    tentacle.y,
    128,
    64
  );
  if (tentacle.donut != null) {
    draw_tentacle_donut(input);
  }
};

const draw_disappointed_state = (input: DrawInput) => {
  const { context, tentacle, disappointed_tentacle_image, tentacle_image } =
    input;
  const frame = Math.min(
    76,
    Math.floor(get_tentacle_frame_time(tentacle) * 15)
  );

  const sx = (frame % 8) * 128;
  const sy = Math.floor(frame / 8) * 64;

  context.drawImage(
    disappointed_tentacle_image,
    sx,
    sy,
    128,
    64,
    tentacle.x,
    tentacle.y,
    128,
    64
  );
};

const update_wait_time = (tentacle: Tentacle, timeIncrement: number) => {
  tentacle.wait_time += (tentacle.wait_forward ? 1 : -1) * timeIncrement;
  if (tentacle.wait_time < 3.8) {
    tentacle.wait_forward = true;
    return;
  }
  if (tentacle.wait_time <= 4.2) {
    return;
  }
  tentacle.wait_forward = false;
  tentacle.wait_count++;
  if (tentacle.wait_count <= 3) {
    return;
  }
  /**
   * Waited too long, give up
   */
  tentacle.state = "disappointed";
  tentacle.time = 0;
  return;
};

const get_tentacle_frame_time = (tentacle: Tentacle) => {
  if (
    tentacle.state == "wait_for_donut" ||
    tentacle.state == "wait_for_donut_timing"
  ) {
    return tentacle.wait_time;
  }
  return tentacle.time;
};
