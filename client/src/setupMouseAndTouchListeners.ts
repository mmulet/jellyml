import { deleteTouch } from "./deleteTouch";
import { MouseOrTouchInput } from "./MouseOrTouchInput";
import { setupTouch } from "./setupTouch";
import { Touches } from "./Touches";

export const setupMouseAndTouchListeners = ({
  touches,
  get_mouse,
  set_mouse,
}: {
  readonly touches: Touches;
  readonly get_mouse: () => MouseOrTouchInput | null;
  readonly set_mouse: (mouse: MouseOrTouchInput | null) => void;
}) => {
  window.addEventListener(
    "touchstart",
    (input: TouchEvent) => {
      const { changedTouches } = input;
      for (const { identifier, clientX, clientY } of changedTouches) {
        touches.set(
          identifier,
          setupTouch({
            clientX,
            clientY,
            affected_a_donut: false,
          })
        );
      }
      input.preventDefault();
    },
    false
  );
  window.addEventListener(
    "touchmove",
    ({ changedTouches }: TouchEvent) => {
      for (const { identifier, clientX, clientY } of changedTouches) {
        const touchInfo = touches.get(identifier);
        if (!touchInfo) {
          continue;
        }
        touches.set(
          identifier,
          setupTouch({
            clientX,
            clientY,
            input: touchInfo,
            affected_a_donut: false,
          })
        );
      }
    },
    false
  );

  window.addEventListener("touchcancel", (a) => deleteTouch(touches, a), false);
  let last_touch_end_time = 0;
  window.addEventListener("touchend", (a) => {
    deleteTouch(touches, a), false;
    /**
     * disable double tap to zoom
     * Still leave in pinch to zoom
     * so the user can still zoom,
     * just don't want the user to
     * accidentally zoom in when
     * tapping the donut
     */
    const now = new Date().getTime();
    if (now - last_touch_end_time <= 500) {
      a.preventDefault();
    }
    last_touch_end_time = now;
  });

  window.addEventListener(
    "mouseenter",
    ({ clientX, clientY }: MouseEvent) => {
      set_mouse(
        setupTouch({
          clientX,
          clientY,
          affected_a_donut: true,
        })
      );
    },
    false
  );

  window.addEventListener(
    "mousemove",
    ({ clientX, clientY }: MouseEvent) => {
      set_mouse(
        setupTouch({
          clientX,
          clientY,
          input: get_mouse() ?? undefined,
          affected_a_donut: true,
        })
      );
    },
    false
  );
  window.addEventListener("mousedown", ({ clientX, clientY }: MouseEvent) => {
    const mouse = get_mouse();
    if (mouse == null) {
      return;
    }
    mouse.affected_a_donut = false;
    set_mouse(mouse);
  });
  window.addEventListener("mouseup", ({ clientX, clientY }: MouseEvent) => {
    const mouse = get_mouse();
    if (mouse == null) {
      return;
    }
    mouse.affected_a_donut = true;
    set_mouse(mouse);
  });

  window.addEventListener(
    "mouseenter",
    ({ clientX, clientY }: MouseEvent) => {
      set_mouse(
        setupTouch({
          clientX,
          clientY,
          affected_a_donut: true,
        })
      );
    },
    false
  );
  window.addEventListener("mouseleave", () => {
    set_mouse(null);
  });
};
