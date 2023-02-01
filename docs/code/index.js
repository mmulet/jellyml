(() => {
  // ../client/src/DonutState.ts
  var eaten = 0;
  var not_eaten = 1;
  var state_to_position = (state) => {
    const item = state.top * 8 + state.right * 4 + state.left * 2 + state.bottom;
    return {
      x: item % 8 * 32,
      y: Math.floor(item / 8) * 32
    };
  };

  // ../client/src/draw_donut.ts
  var draw_donut = (ctx, atlas, donut) => {
    const { x, y } = state_to_position(donut.state);
    ctx.drawImage(atlas, x, y, 32, 32, donut.x, donut.y, 32, 32);
  };

  // ../client/src/makeAnimationCanvas.ts
  var animationCanvasId = "animation-canvas";
  var makeAnimationCanvas = (width, height, ratio) => {
    {
      const canvas2 = document.getElementById(
        animationCanvasId
      );
      if (canvas2) {
        const context2 = canvas2.getContext("2d");
        if (!context2) {
          return null;
        }
        return {
          canvas: canvas2,
          context: context2
        };
      }
    }
    const canvas = makeAnimationCanvasElement(width, height, ratio);
    document.body.appendChild(canvas);
    const context = canvas.getContext("2d");
    if (!context) {
      return null;
    }
    context?.scale(ratio, ratio);
    return {
      canvas,
      context
    };
  };
  var makeAnimationCanvasElement = (width, height, ratio) => {
    const canvas = document.createElement("canvas");
    canvas.id = animationCanvasId;
    canvas.width = width * ratio;
    canvas.height = height * ratio;
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    canvas.style.top = "0";
    canvas.style.left = "0";
    canvas.style.position = "fixed";
    canvas.style.pointerEvents = "none";
    return canvas;
  };

  // ../client/src/deleteTouch.ts
  var deleteTouch = (touches, { changedTouches }) => {
    for (const { identifier } of changedTouches) {
      touches.delete(identifier);
    }
  };

  // ../client/src/setupTouch.ts
  var setupTouch = ({
    clientX,
    clientY,
    input: maybeInput,
    affected_a_donut
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
      affected_a_donut
    };
    if (input) {
      input.difference = {
        x: clientX - input.clientX,
        y: clientY - input.clientY
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

  // ../client/src/setupMouseAndTouchListeners.ts
  var setupMouseAndTouchListeners = ({
    touches,
    get_mouse,
    set_mouse
  }) => {
    window.addEventListener(
      "touchstart",
      (input) => {
        const { changedTouches } = input;
        for (const { identifier, clientX, clientY } of changedTouches) {
          touches.set(
            identifier,
            setupTouch({
              clientX,
              clientY,
              affected_a_donut: false
            })
          );
        }
        input.preventDefault();
      },
      false
    );
    window.addEventListener(
      "touchmove",
      ({ changedTouches }) => {
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
              affected_a_donut: false
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
      const now = new Date().getTime();
      if (now - last_touch_end_time <= 500) {
        a.preventDefault();
      }
      last_touch_end_time = now;
    });
    window.addEventListener(
      "mouseenter",
      ({ clientX, clientY }) => {
        set_mouse(
          setupTouch({
            clientX,
            clientY,
            affected_a_donut: true
          })
        );
      },
      false
    );
    window.addEventListener(
      "mousemove",
      ({ clientX, clientY }) => {
        set_mouse(
          setupTouch({
            clientX,
            clientY,
            input: get_mouse() ?? void 0,
            affected_a_donut: true
          })
        );
      },
      false
    );
    window.addEventListener("mousedown", ({ clientX, clientY }) => {
      const mouse = get_mouse();
      if (mouse == null) {
        return;
      }
      mouse.affected_a_donut = false;
      set_mouse(mouse);
    });
    window.addEventListener("mouseup", ({ clientX, clientY }) => {
      const mouse = get_mouse();
      if (mouse == null) {
        return;
      }
      mouse.affected_a_donut = true;
      set_mouse(mouse);
    });
    window.addEventListener(
      "mouseenter",
      ({ clientX, clientY }) => {
        set_mouse(
          setupTouch({
            clientX,
            clientY,
            affected_a_donut: true
          })
        );
      },
      false
    );
    window.addEventListener("mouseleave", () => {
      set_mouse(null);
    });
  };

  // ../client/src/handle_collisions.ts
  var get_eaten_parts = (donut, x, y) => {
    const x_relative_to_donut = x - (donut.x + 16);
    const y_relative_to_donut = y - (donut.y + 16);
    if (y_relative_to_donut >= 0) {
      if (x_relative_to_donut > y_relative_to_donut) {
        return "right";
      }
      if (x_relative_to_donut >= -y_relative_to_donut) {
        return "bottom";
      }
      return "left";
    }
    if (x_relative_to_donut < y_relative_to_donut) {
      return "left";
    }
    if (x_relative_to_donut <= -y_relative_to_donut) {
      return "top";
    }
    return "right";
  };
  var handle_collisions = ({
    mouse: in_mouse,
    touches: in_touches,
    donuts,
    main_position,
    jelly_sprites
  }) => {
    const un_translated_inputs = [];
    if (in_mouse != null && !in_mouse.affected_a_donut) {
      un_translated_inputs.push(in_mouse);
    }
    for (const [, touch] of in_touches) {
      if (touch.affected_a_donut) {
        continue;
      }
      un_translated_inputs.push(touch);
    }
    if (un_translated_inputs.length <= 0) {
      return;
    }
    const inputs = [];
    for (const input of un_translated_inputs) {
      inputs.push({
        left_x: input.clientX - main_position.left,
        left_y: input.clientY - main_position.top,
        right_x: input.clientX - main_position.right,
        right_y: input.clientY - main_position.top
      });
    }
    const indices_to_remove = [];
    for (let i = 0; i < donuts.length; i++) {
      const donut = donuts[i];
      for (let input_i = 0; input_i < inputs.length; input_i++) {
        const input = inputs[input_i];
        const x = donut.left ? input.left_x : input.right_x;
        const y = donut.left ? input.left_y : input.right_y;
        if (!(x > donut.x && x < donut.x + 32 && y > donut.y && y < donut.y + 32)) {
          continue;
        }
        const part = get_eaten_parts(donut, x, y);
        if (donut.state[part] == eaten) {
          continue;
        }
        jelly_sprites.push({
          x: x - 32,
          y: y - 32,
          age: 0,
          vertical: part == "left" || part == "right" ? true : false,
          left: donut.left
        });
        if (jelly_sprites.length > 500) {
          jelly_sprites.shift();
        }
        donut.state[part] = eaten;
        un_translated_inputs[input_i].affected_a_donut = true;
        if (donut.state.left == eaten && donut.state.right == eaten && donut.state.top == eaten && donut.state.bottom == eaten) {
          indices_to_remove.push(i);
        }
        break;
      }
    }
    indices_to_remove.sort();
    for (let i = indices_to_remove.length - 1; i >= 0; i--) {
      donuts.splice(indices_to_remove[i], 1);
    }
  };

  // ../client/src/DonutMaker.ts
  var update_donut_makers = (donut_makers, timeDifference, on_open) => {
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
  var draw_donut_maker = (ctx, sprites, donutMaker) => {
    const frame = Math.max(Math.min(15, Math.floor(donutMaker.time * 15)), 0);
    const sx = 256 + frame % 8 * 32;
    const sy = Math.floor(frame / 8) * 64;
    ctx.drawImage(sprites, sx, sy, 32, 64, donutMaker.x, donutMaker.y, 32, 64);
  };

  // ../client/src/JellySprite.ts
  var update_jelly_sprites = (sprites, timeIncrement) => {
    let indices_to_remove = [];
    for (let i = 0; i < sprites.length; i++) {
      const jelly = sprites[i];
      jelly.age += timeIncrement;
    }
    for (let i = indices_to_remove.length - 1; i >= 0; i--) {
      sprites.splice(indices_to_remove[i], 1);
      console.log("removing");
    }
  };
  var draw_jelly_sprite = (ctx, sprites, jelly) => {
    if (jelly.vertical) {
      let frame2 = Math.min(3, Math.floor(jelly.age * 15));
      const sx2 = frame2 % 4 * 64;
      const sy2 = 64 + Math.floor(frame2 / 4) * 64;
      ctx.drawImage(sprites, sx2, sy2, 64, 64, jelly.x, jelly.y, 64, 64);
      return;
    }
    let frame = Math.min(3, Math.floor(jelly.age * 15));
    const sx = 256 + frame % 4 * 64;
    const sy = 128 + Math.floor(frame / 4) * 64;
    ctx.drawImage(sprites, sx, sy, 64, 64, jelly.x, jelly.y, 64, 64);
  };

  // ../client/src/find_next_donut.ts
  var find_next_donut = ({
    donut_holder,
    main_position,
    donuts,
    time_threshold,
    animation_length,
    pure_only
  }) => {
    let lowest_possible_donut_index = -1;
    for (let index2 = 0; index2 < donuts.length; index2++) {
      const donut2 = donuts[index2];
      if (donut2.left !== donut_holder.left) {
        continue;
      }
      const y_in_absolute_coords2 = donut2.y + main_position.top;
      if (y_in_absolute_coords2 > donut_holder.y) {
        continue;
      }
      const distance_in_a_second = donut2.vy * animation_length;
      const y_in_a_second = y_in_absolute_coords2 + distance_in_a_second;
      if (y_in_a_second > donut_holder.y) {
        continue;
      }
      if (y_in_absolute_coords2 < donut_holder.y - donut2.vy * time_threshold) {
        continue;
      }
      if (pure_only && (donut2.state.bottom == eaten || donut2.state.left == eaten || donut2.state.right == eaten || donut2.state.top == eaten)) {
        continue;
      }
      if (lowest_possible_donut_index == -1) {
        lowest_possible_donut_index = index2;
        continue;
      }
      const lowest_donut = donuts[lowest_possible_donut_index];
      if (donut2.y >= lowest_donut.y) {
        lowest_possible_donut_index = index2;
      }
    }
    if (lowest_possible_donut_index == -1) {
      return true;
    }
    const index = lowest_possible_donut_index;
    const donut = donuts[index];
    const y_in_absolute_coords = donut.y + main_position.top;
    const x_in_absolute_coords = donut.x + (donut.left ? main_position.left : main_position.right);
    donut.x = x_in_absolute_coords - donut_holder.x;
    donut.y = y_in_absolute_coords - donut_holder.y;
    donut_holder.donut = donut;
    donuts.splice(index, 1);
    return false;
  };

  // ../client/src/animate_tentacles_grabbed_donut.ts
  var frame_positions = {
    72: { x: -1.7321655273437493, y: 9.48956179151348 },
    73: { x: -1.7321655273437493, y: 9.48956179151348 },
    74: { x: -1.7321655273437493, y: 9.48956179151348 },
    75: { x: -1.7321655273437493, y: 9.48956179151348 },
    76: { x: -1.4107849121093743, y: 10.11971986060049 },
    77: { x: -0.1252593994140625, y: 12.797894646139707 },
    78: { x: 2.4457885742187493, y: 16.263770009957113 },
    79: { x: 6.141671752929689, y: 20.98996151194853 },
    80: { x: 11.926531982421874, y: 26.188774557674634 },
    81: { x: 19.478988647460938, y: 31.07250856885723 },
    82: { x: 29.441802978515625, y: 35.641163545496326 },
    83: { x: 40.20807113647461, y: 38.319338331035546 },
    84: { x: 52.58124618530273, y: 38.949496400122555 },
    85: { x: 64.63303833007812, y: 37.37410122740503 },
    86: { x: 76.52413940429688, y: 33.278067794500615 },
    87: { x: 86.0048828125, y: 26.50385957605699 },
    88: { x: 93.39664916992187, y: 19.572111840341606 },
    89: { x: 98.37805786132813, y: 12.010203043619793 },
    90: { x: 100.46703491210937, y: 6.181231928806682 },
    91: { x: 100.78841552734374, y: 2.872897578220744 },
    92: { x: 99.34219970703126, y: 1.9276589786305145 },
    93: { x: 96.28907775878906, y: 3.660596660539216 },
    94: { x: 92.7538848876953, y: 7.441551058900124 },
    95: { x: 87.45109558105469, y: 12.482821595435052 },
    96: { x: 80.22001953125, y: 18.154253192976412 },
    97: { x: 72.34618225097657, y: 22.722905177696084 },
    98: { x: 62.704748535156256, y: 26.66139909332874 },
    99: { x: 53.545385742187506, y: 29.02449484432445 },
    100: { x: 43.74326095581055, y: 29.81219243068321 },
    101: { x: 36.030113220214844, y: 29.49711339613971 },
    102: { x: 28.959729003906247, y: 28.07925474877451 },
    103: { x: 24.62108459472656, y: 26.503856584137566 },
    104: { x: 21.567962646484375, y: 25.243537454044123 },
    105: { x: 19.63967590332031, y: 24.14075784122243 },
    106: { x: 18.99691467285156, y: 22.88043871112899 },
    107: { x: 19.63967590332031, y: 21.62011958103554 },
    108: { x: 21.728652954101562, y: 20.674882477405028 },
    109: { x: 24.460392761230466, y: 20.044724408318018 },
    110: { x: 28.316966247558597, y: 18.469326243681067 },
    111: { x: 33.13768310546875, y: 17.681628657322307 },
    112: { x: 37.95839996337891, y: 17.209010105507048 },
    113: { x: 42.61842651367188, y: 16.578852036420038 },
    114: { x: 47.27845306396485, y: 16.263773001876537 },
    115: { x: 50.65295524597168, y: 16.263773001876537 },
    116: { x: 53.8667667388916, y: 15.160993389054841 },
    117: { x: 55.955744171142584, y: 12.955437155330884 },
    118: { x: 56.91988754272461, y: 8.386785170611216 },
    119: { x: 56.598506164550784, y: 3.818133185891547 },
    120: { x: 54.34883804321289, y: -1.8532984116498152 },
    121: { x: 50.97433586120606, y: -7.3671897439395675 },
    122: { x: 46.7963809967041, y: -11.778302585377412 },
    123: { x: 42.618426132202146, y: -14.771557901419845 },
    124: { x: 39.88668670654297, y: -17.292193917667163 },
    125: { x: 39.08323364257812, y: -19.3402110081093 },
    126: { x: 37.73278274536133, y: -22.919728447409238 },
    127: { x: 36.073744201660155, y: -26.76318479051777 },
    128: { x: 35.26352996826172, y: -28.55819881663603 },
    129: { x: 35.26352996826172, y: -28.55819881663603 },
    130: { x: 35.26352996826172, y: -32 }
  };
  var animate_tentacles_grabbed_donut = ({
    donut,
    time,
    x,
    y
  }) => {
    if (donut === null) {
      return;
    }
    const frame = Math.min(130, Math.floor(time * 15));
    const frame_position = frame_positions[frame];
    if (frame_position === void 0) {
      return;
    }
    donut.x = frame_position.x;
    donut.y = frame_position.y;
  };

  // ../client/src/draw_tentacle_donut.ts
  var draw_tentacle_donut = ({
    context,
    tentacle,
    sprites,
    tentacle_line
  }) => {
    const donut = tentacle.donut;
    const { x, y } = state_to_position(donut.state);
    const donut_x = donut.x + tentacle.x;
    const donut_y = donut.y + tentacle.y;
    context.drawImage(sprites, x, y, 32, 32, donut_x, donut_y, 32, 32);
    const eye_frame = tentacle.state === "grabbing_donut" ? 0 : 1;
    context.drawImage(
      sprites,
      512 - 64 + eye_frame * 32,
      512 - 32,
      32,
      32,
      donut_x + Math.random() * 2,
      donut_y + Math.random() * 2,
      32,
      32
    );
    const line = 14 * (1 - tentacle.donut_find_time / 0.2);
    if (line > 0) {
      context.drawImage(sprites, x, y, 32, line, donut_x, donut_y, 32, line);
    }
    if (tentacle.time * 15 < 121) {
      return;
    }
    const { bottom } = tentacle_line.getBoundingClientRect();
    context.clearRect(donut_x, bottom - 32, 32, 32);
  };

  // ../client/src/Tentacle.ts
  var update_tentacle = (input, timeIncrement) => {
    const { tentacle, main_position, donuts, tentacle_line } = input;
    if (tentacle.state === "finished") {
      return;
    }
    const line = tentacle_line.getBoundingClientRect();
    tentacle.x = main_position.left;
    tentacle.y = line.bottom;
    switch (tentacle.state) {
      case "wait_for_scroll":
        if (line.top > 400) {
          return;
        }
        tentacle.state = "animating_1";
      case "animating_1":
        tentacle.time += timeIncrement;
        if (tentacle.time < 4) {
          return;
        }
        tentacle.state = "wait_for_donut";
        tentacle.wait_time = tentacle.time;
      case "wait_for_donut":
        const next_donut = find_next_donut({
          donut_holder: tentacle,
          main_position,
          donuts,
          animation_length: 0.7,
          time_threshold: 0.8,
          pure_only: true
        });
        if (next_donut) {
          update_wait_time(tentacle, timeIncrement);
          return;
        }
        tentacle.state = "wait_for_donut_timing";
      case "wait_for_donut_timing":
        tentacle.donut.y += tentacle.donut.vy * timeIncrement;
        tentacle.donut_find_time += timeIncrement;
        if (tentacle.donut.y + tentacle.donut.vy * 0.7 < 0) {
          update_wait_time(tentacle, timeIncrement);
          return;
        }
        tentacle.state = "animating_2";
      case "animating_2":
        tentacle.donut.y += tentacle.donut.vy * timeIncrement;
        if (tentacle.time < 4.8) {
          tentacle.time += timeIncrement;
          return;
        }
        tentacle.state = "grabbing_donut";
      case "grabbing_donut":
        tentacle.time += timeIncrement;
        animate_tentacles_grabbed_donut(tentacle);
        if (tentacle.time < 10) {
          return;
        }
        tentacle.state = "finished";
        return;
      case "disappointed":
        tentacle.time += timeIncrement;
        if (tentacle.time < 5.07) {
          return;
        }
        tentacle.state = "finished";
        return;
    }
  };
  var draw_tentacle = (input) => {
    const { context, tentacle, sprites, tentacle_image, tentacle_line } = input;
    if (tentacle.state === "finished") {
      return;
    }
    if (tentacle.state === "disappointed") {
      draw_disappointed_state(input);
      return;
    }
    const frame = Math.min(
      127,
      Math.floor(get_tentacle_frame_time(tentacle) * 15)
    );
    const sx = frame % 8 * 128;
    const sy = Math.floor(frame / 8) * 64;
    context.drawImage(
      tentacle_image,
      sx,
      sy,
      128,
      64,
      tentacle.x,
      tentacle.y,
      128,
      64
    );
    if (tentacle.donut != null) {
      draw_tentacle_donut(input);
    }
  };
  var draw_disappointed_state = (input) => {
    const { context, tentacle, disappointed_tentacle_image, tentacle_image } = input;
    const frame = Math.min(
      76,
      Math.floor(get_tentacle_frame_time(tentacle) * 15)
    );
    const sx = frame % 8 * 128;
    const sy = Math.floor(frame / 8) * 64;
    context.drawImage(
      disappointed_tentacle_image,
      sx,
      sy,
      128,
      64,
      tentacle.x,
      tentacle.y,
      128,
      64
    );
  };
  var update_wait_time = (tentacle, timeIncrement) => {
    tentacle.wait_time += (tentacle.wait_forward ? 1 : -1) * timeIncrement;
    if (tentacle.wait_time < 3.8) {
      tentacle.wait_forward = true;
      return;
    }
    if (tentacle.wait_time <= 4.2) {
      return;
    }
    tentacle.wait_forward = false;
    tentacle.wait_count++;
    if (tentacle.wait_count <= 3) {
      return;
    }
    tentacle.state = "disappointed";
    tentacle.time = 0;
    return;
  };
  var get_tentacle_frame_time = (tentacle) => {
    if (tentacle.state == "wait_for_donut" || tentacle.state == "wait_for_donut_timing") {
      return tentacle.wait_time;
    }
    return tentacle.time;
  };

  // ../client/src/load_image.ts
  var load_image = (path) => {
    const image = new Image();
    image.src = path;
    return image;
  };

  // ../client/src/UFO.ts
  var update_ufos = ({ ufos, main_position, donuts }, timeDifference) => {
    for (const ufo of ufos) {
      ufo.time += timeDifference;
      ufo.y = main_position.bottom - 100;
      ufo.x = ufo.left ? main_position.left - 16 : main_position.right - 16;
      switch (ufo.abducting_state) {
        case "waiting":
          const next_donut = find_next_donut({
            donut_holder: ufo,
            main_position,
            donuts,
            animation_length: 0.2,
            time_threshold: 0.3,
            pure_only: false
          });
          if (next_donut) {
            continue;
          }
          ufo.abducting_state = "wait_for_abduct";
        case "wait_for_abduct":
          ufo.donut.y += ufo.donut.vy * timeDifference;
          ufo.wait_time += timeDifference;
          if (ufo.wait_time > 0.4) {
            ufo.abducting_time += timeDifference;
          }
          if (ufo.wait_time < 1.1) {
            continue;
          }
          ufo.abducting_state = "abducting";
        case "abducting":
          ufo.abducting_time += timeDifference;
          if (ufo.abducting_time < 1.94) {
            continue;
          }
          ufo.abducting_state = "waiting";
          ufo.wait_time = 0;
          ufo.abducting_time = 0;
          ufo.donut = null;
          return;
      }
    }
  };
  var draw_ufos = (input) => {
    const { context, sprites, ufos } = input;
    for (const ufo of ufos) {
      if (ufo.donut) {
        draw_ufo_donut(input, ufo);
      }
      {
        const frame2 = Math.floor(ufo.abducting_time * 15) % 30;
        const sx2 = 256 + 32 * (frame2 % 8);
        const sy2 = 64 * 3 + 64 * Math.floor(frame2 / 8);
        context.drawImage(
          sprites,
          sx2,
          sy2,
          32,
          64,
          ufo.x + 16,
          ufo.y + 45,
          32,
          64
        );
      }
      const raw_frame = Math.floor(ufo.time * 10) % 19;
      const frame = ufo.clockwise ? raw_frame : 18 - raw_frame;
      const sx = 64 * (frame % 4);
      const sy = 128 + 64 * Math.floor(frame / 4);
      context.drawImage(sprites, sx, sy, 64, 64, ufo.x, ufo.y, 64, 64);
    }
  };
  var donut_abduct_animation = {
    22: { x: 4, y: -20, size: 24 },
    23: { x: 8, y: -25.6, size: 16 },
    24: { x: 10, y: -29.85, size: 12 },
    25: { x: 10, y: -32.45, size: 12 },
    26: { x: 12, y: -38.25, size: 8 },
    27: { x: 12, y: -44.25, size: 8 },
    28: { x: 14, y: -53.84, size: 4 },
    29: { x: 14, y: -62.8, size: 4 }
  };
  var get_abduct_animation_offsets = (ufo) => {
    const default_offset = { x: 0, y: 0, size: 32 };
    if (ufo.abducting_state !== "abducting") {
      return default_offset;
    }
    const frame = Math.floor(ufo.abducting_time * 15) % 30;
    return donut_abduct_animation[frame] ?? default_offset;
  };
  var draw_ufo_donut = ({ context, sprites }, ufo) => {
    const donut = ufo.donut;
    const { x, y } = state_to_position(donut.state);
    const { x: x_o, y: y_o, size } = get_abduct_animation_offsets(ufo);
    context.drawImage(
      sprites,
      x,
      y,
      32,
      32,
      donut.x + x_o + ufo.x,
      donut.y + y_o + ufo.y,
      size,
      size
    );
  };

  // ../client/src/Controller.ts
  var Controller = class {
    constructor() {
      this.touches = /* @__PURE__ */ new Map();
      this.mouse = null;
      this.lastFrameTime = null;
      this.timeSinceLastAnimationFrame = 0;
      this.donut_makers = [
        {
          x: 0,
          y: -32,
          left: true,
          time: 0,
          state: "open",
          just_opened: false
        },
        {
          x: 0,
          y: -32,
          left: false,
          time: -1,
          state: "open",
          just_opened: false
        }
      ];
      this.ufos = [
        {
          x: 0,
          y: 0,
          time: 0,
          left: true,
          clockwise: true,
          donut: null,
          abducting_time: 0,
          abducting_state: "waiting",
          wait_time: 0
        },
        {
          x: 0,
          y: 0,
          time: 0,
          left: false,
          clockwise: false,
          donut: null,
          abducting_time: 0,
          abducting_state: "waiting",
          wait_time: 0
        },
        {
          x: 0,
          y: 0,
          time: 0,
          left: true,
          clockwise: true,
          donut: null,
          abducting_time: 0,
          abducting_state: "waiting",
          wait_time: 0
        },
        {
          x: 0,
          y: 0,
          time: 0,
          left: false,
          clockwise: false,
          donut: null,
          abducting_time: 0,
          abducting_state: "waiting",
          wait_time: 0
        }
      ];
      this.jelly_sprites = [];
      this.tentacle = {
        x: 0,
        y: 0,
        left: true,
        state: "wait_for_scroll",
        time: 0,
        wait_time: 0,
        wait_forward: true,
        wait_count: 0,
        donut_find_time: 0,
        donut: null
      };
      this.main = document.getElementById("main");
      this.animation_toggle = document.getElementById(
        "animation-toggle"
      );
      this.animation_disabled = false;
      this.main_position = {
        left: 0,
        top: 0,
        right: 0,
        bottom: 0
      };
      this.donuts = [];
      this.sprites = load_image("/static/sprites.png");
      this.tentacle_image = load_image("/static/tentacle.png");
      this.disappointed_tentacle_image = load_image("/static/tentacle_disappointed.png");
      this.tentacle_line = document.getElementById("tentacle-line");
      this.updateStateAndDraw = (totalTimeElapsed) => {
        if (this.animation_disabled) {
          this.context.clearRect(0, 0, this.width, this.height);
          return;
        }
        this.updateState(totalTimeElapsed);
        this.draw();
        requestAnimationFrame(this.updateStateAndDraw);
      };
      this.updateState = (totalTimeElapsed) => {
        const timeDifference = this.lastFrameTime == null ? 0 : totalTimeElapsed - this.lastFrameTime;
        this.lastFrameTime = totalTimeElapsed;
        const timeIncrement = timeDifference / 1e3;
        this.timeSinceLastAnimationFrame += timeIncrement;
        const main_client_rect = this.main.getBoundingClientRect();
        this.main_position = {
          left: main_client_rect.left,
          top: main_client_rect.top,
          right: main_client_rect.right - 32,
          bottom: main_client_rect.bottom - 32
        };
        handle_collisions(this);
        for (const donut of this.donuts) {
          donut.y += timeIncrement * donut.vy;
        }
        update_donut_makers(this.donut_makers, timeIncrement, this.spawn_donut);
        update_jelly_sprites(this.jelly_sprites, timeIncrement);
        update_tentacle(this, timeIncrement);
        update_ufos(this, timeIncrement);
        for (const [_, touch] of this.touches) {
          touch.difference = null;
        }
        if (this.mouse) {
          this.mouse.difference = null;
        }
      };
      this.spawn_donut = (maker) => {
        const donut = {
          x: maker.x,
          y: maker.y + 32,
          vy: 100,
          state: {
            top: not_eaten,
            right: not_eaten,
            left: not_eaten,
            bottom: not_eaten
          },
          left: maker.left
        };
        this.donuts.push(donut);
      };
      this.draw_side = (left) => {
        for (const jelly_sprite of this.jelly_sprites) {
          if (jelly_sprite.left != left) {
            continue;
          }
          draw_jelly_sprite(this.context, this.sprites, jelly_sprite);
        }
        for (const maker of this.donut_makers) {
          if (maker.left != left) {
            continue;
          }
          draw_donut_maker(this.context, this.sprites, maker);
        }
        for (const donut of this.donuts) {
          if (donut.left != left) {
            continue;
          }
          draw_donut(this.context, this.sprites, donut);
        }
      };
      this.draw = () => {
        this.context.setTransform(this.original_transform);
        this.context.clearRect(0, 0, this.width, this.height);
        const zoom = window.visualViewport?.scale || 1;
        if (zoom != 1) {
          return;
        }
        const left_position = {
          x: this.main_position.left,
          y: this.main_position.top
        };
        const right_position = {
          x: this.main_position.right,
          y: this.main_position.top
        };
        this.context.translate(left_position.x, left_position.y);
        this.draw_side(true);
        this.context.translate(
          -left_position.x + right_position.x,
          -left_position.y + right_position.y
        );
        this.draw_side(false);
        this.context.translate(-right_position.x, -right_position.y);
        draw_tentacle(this);
        draw_ufos(this);
      };
      const ratio = window.devicePixelRatio || 1;
      const longest_side = Math.max(screen.width, screen.height);
      this.width = longest_side;
      this.height = longest_side;
      const maybeContext = makeAnimationCanvas(this.width, this.height, ratio);
      if (!maybeContext) {
        throw new Error("Could not make Animation canvas");
      }
      this.context = maybeContext.context;
      this.context.imageSmoothingEnabled = false;
      this.context.fillStyle = "white";
      setupMouseAndTouchListeners({
        touches: this.touches,
        get_mouse: () => this.mouse,
        set_mouse: (mouse) => this.mouse = mouse
      });
      this.animation_toggle.addEventListener("change", ({ target }) => {
        this.animation_disabled = !target.checked;
        if (this.animation_disabled) {
          return;
        }
        this.lastFrameTime = null;
        requestAnimationFrame(this.updateStateAndDraw);
      });
      this.original_transform = this.context.getTransform();
      requestAnimationFrame(this.updateStateAndDraw);
    }
  };

  // ../client/src/index.ts
  var controller = null;
  window.onload = () => {
    if (matchMedia("(prefers-reduced-motion)").matches) {
      return;
    }
    controller = new Controller();
  };
})();
//# sourceMappingURL=index.js.map
