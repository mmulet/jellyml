import markdown_it from "markdown-it";
import highlight_plugin from "markdown-it-highlightjs";
import anchor_plugin from "markdown-it-anchor";

export const markdown_transform = (
  text: string,
  options: {
    levels?: number;
  }
) => {
  const markdown_renderer = markdown_it();
  markdown_renderer.use(highlight_plugin);
  markdown_renderer.use(anchor_plugin, {
    permalink: anchor_plugin.permalink.headerLink({
        safariReaderFix: true,
        class: "header-anchor",
    }),
  });
  return markdown_renderer.render(text);
};
