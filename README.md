# AI-Assignment-3
AI Search Algorithms (BFS &amp; DFS)
# AI Assignment 3 – Search Algorithms

## 📘 About this Project

This assignment is based on basic search algorithms in Artificial Intelligence.
The main goal is to understand how pathfinding works in graphs and real-world environments.

In this project, I have implemented:

* Dijkstra Algorithm (Uniform Cost Search)
* UGV Navigation in Static Environment
* UGV Navigation in Dynamic Environment

---

## 📂 Files Included

* **Cities.csv** → Contains city-to-city distances
* **dijkstra_india.py** → Finds shortest path between cities
* **dynamic_ugv.py** → Simulates pathfinding in a grid with obstacles
* **UGV.py** → Basic grid navigation

---

## 🔍 Dijkstra Algorithm

This algorithm is used to find the shortest path from a source city to all other cities.

It works by:

* Starting from a source node
* Visiting the nearest node first
* Updating distances step by step

It is commonly used in:

* Google Maps
* Network routing
* AI pathfinding

---

## 🤖 UGV Navigation (Static)

In this part, a grid is created where:

* The start and goal positions are fixed
* Obstacles do not change

The algorithm finds a path avoiding obstacles.

---

## 🤖 UGV Navigation (Dynamic)

This is similar to the static case, but:

* Obstacles are generated randomly
* The environment can change

This makes it closer to real-world AI problems.

---

## ▶️ How to Run

Run these commands:

```bash id="run123"
python dijkstra_india.py
python dynamic_ugv.py
```

---

## 📌 What I Learned

* How shortest path algorithms work
* Difference between static and dynamic environments
* How AI can be used for navigation problems

---

## ✅ Conclusion

This assignment helped me understand how search algorithms are applied in real-world scenarios like maps and robotics.

---

## 👨‍💻 Author

**G CHAITRA DARSHAN REDDY (SE24UCSE050)**
