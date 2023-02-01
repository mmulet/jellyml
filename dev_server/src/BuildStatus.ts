import chalk from "chalk";

const icons = ["⣄", "⣤", "⣦", "⣶", "⣷", "⣿"];

const colors = [
  "#4DD0E1",
  "#4FC3F7",
  "#80CBC4",
  "#BDBDBD",
  "#B0BEC5",
  "#FF7043",
  "#81C784",
  "#81C784",
  "#BA68C8",
  "#448AFF",
  "#00E676",
  "#FF6E40",
  "#B2DFDB",
  "#81D4FA",
  "#7986CB",
  "#EC407A",
  "#4DB6AC",
  "#EEFF41",
  "#FFA726",
  "#BCAAA4",
  "#78909C",
  "#00B0FF",
  "#2979FF",
  "#7E57C2",
  "#29B6F6",
  "#4DD0E1",
  "#3F51B5",
  "#64B5F6",
].map((color) => chalk.hex(color));

/**
 * Totally unnecessary class to print a build status as a race among different
 * colors.
 */
export class BuildStatus {
  current_track_color = chalk.white; //colors[Math.floor(Math.random() * icons.length)];

  racers: {
    position: number;
    color: typeof colors[number];
  }[] = [];

  constructor() {
    this.reset_race();
  }

  reset_race() {
    this.racers = [];
    for (let i = 0; i < process.stdout.rows - 1; i++) {
      this.racers.push({
        position: 0,
        color: colors[i % colors.length],
      });
    }
  }

  print_build_number() {
    const number_of_rows = process.stdout.rows - 1;
    const number_of_columns = process.stdout.columns;
    this.update_race_status(number_of_rows, number_of_columns);

    const out = [];
    for (let i = 0; i < number_of_rows; i++) {
      const row = [];
      const racer = this.racers[i];
      for (let j = 0; j < number_of_columns; j++) {
        if (racer.position === j) {
          row.push(
            racer.color(icons[Math.floor(Math.random() * icons.length)])
          );
          continue;
        }
        row.push(this.current_track_color("⣀"));
      }
      out.push(row.join(""));
    }
    console.log(out.join("\n"));
  }

  update_race_status(number_of_rows: number, number_of_columns: number) {
    const num_new_racers = number_of_rows - this.racers.length;
    if (num_new_racers > 0) {
      const last_place = this.racers.reduce(
        (acc, racer) => Math.min(acc, racer.position),
        0
      );
      for (let i = 0; i < num_new_racers; i++) {
        this.racers.push({
          position: Math.max(0, last_place - 1),
          color: colors[Math.floor(Math.random() * icons.length)],
        });
      }
    }
    for (const racer of this.racers) {
      racer.position += Math.floor(Math.random() * 3);
      if (racer.position > number_of_columns) {
        this.current_track_color = racer.color;
        this.reset_race();
        return;
      }
    }
  }
}
