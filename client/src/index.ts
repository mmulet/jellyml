import { Controller } from "./Controller";

let controller: Controller | null = null;

window.onload = () => {
  if (matchMedia("(prefers-reduced-motion)").matches) {
    return;
  }
  controller = new Controller();
};
