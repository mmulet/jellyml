export interface MouseOrTouchInput {
  left: number;
  right: number;
  top: number;
  bottom: number;
  clientX: number;
  clientY: number;
  difference: {
    x: number;
    y: number;
  } | null;
  affected_a_donut: boolean;
}
