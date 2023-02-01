import { Touches } from "./Touches";

export const deleteTouch = (
  touches: Touches,
  { changedTouches }: TouchEvent
) => {
  for (const { identifier } of changedTouches) {
    touches.delete(identifier);
  }
};
