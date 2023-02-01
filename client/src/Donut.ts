import { DonutState } from "./DonutState";


/**
 * Position (x,y) of the donut is relative to 
 * the parent. The parent depends on where
 * the donut is. If it's in the main donuts,
 * it's relative to the left or right side of
 * of the menu. If it's in the tentacle, it's
 * relative to the tentacle.
 * If it's in the ufo it's relative to the ufo.
 */
export interface Donut {
  x: number;
  y: number;
  vy: number;
  state: DonutState;
  /**
   * Donut can be on the left side of the screen
   * or the right side of the screen
   */
  left: boolean;
}
