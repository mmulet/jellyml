setInterval(() => {
  const reloadNumber = "replaceReloadNumber";
  fetch(`/replaceReloadPath`)
    .then((res) => res.text())
    .then((text) => {
      if (text !== reloadNumber) {
        //reload the page
        window.location.reload();
      }
    });
}, 100);
