const fullText = "hi, antonius riki hermawan here.";
const typedEl = document.getElementById("typed-text");
let index = 0;

function type() {
  if (index < fullText.length) {
    const char = fullText.charAt(index);
    let htmlToAdd = char; // Defaultnya, tambahkan karakter biasa

    // Untuk 'hi,' (indeks 0, 1, 2) dan 'here.' (indeks 28, 29, 30, 31)
    if ((index >= 0 && index <= 2) || (index >= 27 && index <= 31)) {
      htmlToAdd = `<span style="color: white;">${char}</span>`;
    }
    // Untuk 'antonius riki hermawan' (indeks 4 sampai 27)
    else if (index >= 4 && index <= 26) {
      htmlToAdd = `<span style="font-weight: bold;">${char}</span>`;
    }

    typedEl.innerHTML += htmlToAdd;
    index++;
    setTimeout(type, 100);
  }
}

function sayHi() {
  alert("Thanks for reaching out! ✨");
}

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("bg-dark");
  } else {
    navbar.classList.remove("bg-dark");
  }
});

const projects = [
  {
    title: "Clone Website Dicoding",
    image: "/static/assets/image/project1.png",
    link: "https://github.com/antoniusrikihermawan",
  },
  {
    title: "Bali Travel",
    image: "/static/assets/image/project2.png",
    link: "https://github.com/antoniusrikihermawan/UAS-CSP.git",
  },
  {
    title: "Portofolio Website",
    image: "/static/assets/image/project3.png",
    link: "https://github.com/antoniusrikihermawan/portofolio-ytCodehal.git",
  },
];

let currentIndex = 0;

function updateShowcase() {
  const showcaseImg = document.getElementById("showcase-img");
  const showcaseTitle = document.getElementById("showcase-title");
  const showcaseLink = document.getElementById("showcase-link");

  const project = projects[currentIndex];
  showcaseImg.src = project.image;
  showcaseTitle.textContent = project.title;
  showcaseLink.href = project.link;
}

function nextProject() {
  currentIndex = (currentIndex + 1) % projects.length;
  updateShowcase();
}

function prevProject() {
  currentIndex = (currentIndex - 1 + projects.length) % projects.length;
  updateShowcase();
}

// Inisialisasi showcase saat halaman load
document.addEventListener("DOMContentLoaded", () => {
  updateShowcase();
  type();
});
