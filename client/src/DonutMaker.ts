export interface DonutMaker {
  x: number;
  y: number;
  left: boolean;
  time: number;
  state: "open" | "close" | "idle";
  just_opened: boolean;
}

export const update_donut_makers = (
  donut_makers: DonutMaker[],
  timeDifference: number,
  on_open: (donutMaker: DonutMaker) => void
) => {
  for (const donutMaker of donut_makers) {
    switch (donutMaker.state) {
      case "idle":
        continue;
      case "open":
        donutMaker.time += timeDifference;
        if (!donutMaker.just_opened && donutMaker.time * 15 > 7) {
          donutMaker.just_opened = true;
          on_open(donutMaker);
        }
        if (donutMaker.time * 15 > 15) {
          donutMaker.state = "close";
          donutMaker.just_opened = false;
        }
        continue;
      case "close":
        donutMaker.time -= timeDifference;
        if (donutMaker.time < 0) {
          donutMaker.time = 0;
          donutMaker.state = "open";
        }
        continue;
    }
  }
};

export const draw_donut_maker = (
  ctx: CanvasRenderingContext2D,
  sprites: HTMLImageElement,
  donutMaker: DonutMaker
) => {
  /**
   * 15 fps
   */
  const frame = Math.max(Math.min(15, Math.floor(donutMaker.time * 15)), 0);
  const sx = 256 + (frame % 8) * 32;
  const sy = Math.floor(frame / 8) * 64;

  ctx.drawImage(sprites, sx, sy, 32, 64, donutMaker.x, donutMaker.y, 32, 64);
};
