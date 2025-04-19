(function () {
  document.addEventListener("DOMContentLoaded", function () {
      $("a.reference.external").each(function () {
        $(this).attr("target", "_blank")
      })
  })
})()