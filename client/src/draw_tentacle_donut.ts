import { state_to_position } from "./DonutState";
import { DrawInput } from "./Tentacle";

export const draw_tentacle_donut = ({
  context,
  tentacle,
  sprites,
  tentacle_line,
}: DrawInput) => {
  const donut = tentacle.donut!;
  /**
   * same as draw_donut
   */
  const { x, y } = state_to_position(donut.state);
  const donut_x = donut.x + tentacle.x;
  const donut_y = donut.y + tentacle.y;
  context.drawImage(sprites, x, y, 32, 32, donut_x, donut_y, 32, 32);
  /**
   * Draw the donut's eyes
   */
  const eye_frame = tentacle.state === "grabbing_donut" ? 0 : 1;
  context.drawImage(
    sprites,
    512 - 64 + eye_frame * 32,
    512 - 32,
    32,
    32,
    donut_x + Math.random() * 2,
    donut_y + Math.random() * 2,
    32,
    32
  );
  /**
   * Draw the top part of the donut so it looks
   * like the donut is opening it's eyes
   */
  const line = 14 * (1 - tentacle.donut_find_time / 0.2);
  if (line > 0) {
    context.drawImage(sprites, x, y, 32, line, donut_x, donut_y, 32, line);
  }

  if (tentacle.time * 15 < 121) {
    /**
     * Make the donut look like it's disappearing under
     * the line, grabbed by the tentacle
     */
    return;
  }
  const { bottom } = tentacle_line.getBoundingClientRect();
  context.clearRect(donut_x, bottom - 32, 32, 32);
};
