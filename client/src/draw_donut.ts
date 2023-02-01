import { Donut } from "./Donut";
import { state_to_position } from "./DonutState";
export const draw_donut = (
  ctx: CanvasRenderingContext2D,
  atlas: HTMLImageElement,
  donut: Donut
) => {
  const { x, y } = state_to_position(donut.state);
  ctx.drawImage(atlas, x, y, 32, 32, donut.x, donut.y, 32, 32);
};
