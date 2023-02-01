import { MouseOrTouchInput } from "./MouseOrTouchInput";

export const setupTouch = ({
  clientX,
  clientY,
  input: maybeInput,
  affected_a_donut,
}: {
  readonly clientX: number;
  readonly clientY: number;
  readonly input?: MouseOrTouchInput;
  readonly affected_a_donut: boolean;
}) => {
  const touchWidth = 20;
  const input = maybeInput ?? {
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    clientX: 0,
    clientY: 0,
    difference: null,
    frameValid: false,
    affected_a_donut,
  };
  if (input) {
    input.difference = {
      x: clientX - input.clientX,
      y: clientY - input.clientY,
    };
  }
  input.clientX = clientX;
  input.clientY = clientY;
  input.left = clientX - touchWidth;
  input.right = clientX + touchWidth;
  input.top = clientY - touchWidth;
  input.bottom = clientY + touchWidth;
  return input;
};
