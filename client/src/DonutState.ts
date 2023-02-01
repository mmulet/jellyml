export type Eaten = 0;
export type Not_Eaten = 1;

export const eaten: Eaten = 0;
export const not_eaten: Not_Eaten = 1;

export type EatenState = Eaten | Not_Eaten;

export interface DonutState {
  top: EatenState;
  right: EatenState;
  left: EatenState;
  bottom: EatenState;
}
/**
 * position is in binary
 * top right left bottom
 * in that order, top is most significant
 * bottom is least significant
 * 1111 is not eaten
 * 0000 is eaten
 *
 */
export const state_to_position = (state: DonutState) => {
  const item =
    (state.top * 8 + state.right * 4 + state.left * 2 + state.bottom);
  return {
    x: (item % 8) * 32,
    y: Math.floor(item / 8) * 32,
  };
};
