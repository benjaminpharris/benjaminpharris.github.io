---
layout: home
title: Home
---

## About Me (Briefly)
I’m a data scientist who blends statistics, finance, and bad humor. This is where I share some of the projects I build in Python (and R) — from statistical modeling to fractal explorers.

* 📈 Finance, modeling, and market structure
* 🧪 Experimentation and statistical inference
* 🧠 Human-centered insight through data

---

## Projects

<div class="project-grid">
  <div class="project-card">
    <h3>🌀 Mandelbrot Explorer</h3>
    <p>A fully interactive fractal generator built in Streamlit with real-time parameter controls.</p>
    <p>
      <a href="https://benjaminpharrisappio-zkmtudj8gmzptl39vwndpp.streamlit.app/" target="_blank">Live Demo</a> | <a href="https://github.com/benjaminpharris/benjaminpharris.github.io/tree/main/mandlebrot-app" target="_blank">Source Code</a>
    </p>
  </div>

  <div class="project-card">
    <h3>📈 Marketing Mix Model</h3>
    <p>A real-world media ROI model using adstock, Bayesian priors, and random forest estimation.</p>
    <p>
      <a href="#" target="_blank">Demo Coming Soon</a> | <a href="https://github.com/benjaminpharris/mmm-model" target="_blank">Source Code</a> 
    </p>
  </div>

  </div>

---

## Blog Posts

<ul class="post-list">
  {% for post in site.posts limit: 5 %} 
    <li>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      {% if post.excerpt %}
        <p>{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
      {% endif %}
    </li>
  {% endfor %}
</ul>
<p><a href="{{ '/blog/' | relative_url }}">View All Posts...</a></p> 