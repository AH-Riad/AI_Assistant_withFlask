document.getElementById("askForm").onsubmit = async (e) => {
  e.preventDefault();

  let formData = new FormData(e.target);
  let loading = document.getElementById("ans-loading");
  loading.style.display = "block";

  let res = await fetch("/ask", {
    method: "POST",
    body: formData,
  });

  let data = await res.json();

  const answer = document.getElementById("answer");

  const html = marked.parse(data.response);
  answer.innerHTML = DOMPurify.sanitize(html);

  loading.style.display = "none";
  e.target.reset();
};

document.getElementById("emailForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  let formData = new FormData(e.target);
  let loading = document.getElementById("summary-loading");
  loading.style.display = "block";

  let res = await fetch("/summarize", {
    method: "POST",
    body: formData,
  });

  let data = await res.json();

  const summary = document.getElementById("summary");

  const html = marked.parse(data.response);
  summary.innerHTML = DOMPurify.sanitize(html);

  loading.style.display = "none";
  e.target.reset();
});
