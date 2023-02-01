export const load_image = (path: string) => {
  const image = new Image();
  image.src = path;
  return image;
};
