export interface JellySprite {
  x: number;
  y: number;

  age: number;
  vertical: boolean;
  left: boolean;
}

export const update_jelly_sprites = (
  sprites: JellySprite[],
  timeIncrement: number
) => {
  let indices_to_remove: number[] = [];
  for (let i = 0; i < sprites.length; i++) {
    const jelly = sprites[i];

    jelly.age += timeIncrement;
  }
  /**
   * remove backwards so that the indices don't change
   */
  for (let i = indices_to_remove.length - 1; i >= 0; i--) {
    sprites.splice(indices_to_remove[i], 1);
    console.log("removing");
  }
};

/**
 * Some weird variable frame rate stuff because
 * I don't like how it looks when it's constant
 */
export const draw_jelly_sprite = (
  ctx: CanvasRenderingContext2D,
  sprites: HTMLImageElement,
  jelly: JellySprite
) => {
  if (jelly.vertical) {
    let frame = Math.min(3, Math.floor(jelly.age * 15));
    const sx = (frame % 4) * 64;
    const sy = 64 + Math.floor(frame / 4) * 64;
    ctx.drawImage(sprites, sx, sy, 64, 64, jelly.x, jelly.y, 64, 64);
    return;
  }
  /**
   * 15 fps
   */
  let frame = Math.min(3, Math.floor(jelly.age * 15));
  const sx = 256 + (frame % 4) * 64;
  const sy = 128 + Math.floor(frame / 4) * 64;

  ctx.drawImage(sprites, sx, sy, 64, 64, jelly.x, jelly.y, 64, 64);
};
