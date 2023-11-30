% **CS 437: Internet of Things** \
  **Final Project Report**
---
urlcolor: cyan
---

## Team

* Eric Schrock (ejs9)
* Devin Schmitz (devinms3)


## Overview

We created a distributed network of CO2 sensors that report back via wifi to a central hub. The hub exposes a web interface on the LAN for accessing the data. This allows us to track variations in CO2 levels throughout a home and over time. This data could be used to understand and improve indoor air quality, leading to healthier lives.


## Motivation

todo: "Talk about the importance of this problem. Pretend you are trying to convince someone to give you funding, or purchase what you developed. You may also want to give references/citations here."

todo: Rehash motivation section from the proposal. Maybe remove "low energy" as a design goal.


## Technical Approach

todo: "Describe the technical approach you used to complete your work.
You can give your overall architecture, describe how data flows through your system,
describe algorithms you developed, provide circuit diagrams, etc. Provide anything
important in understanding *how* you did what you did."


## Implementation Details

todo: "This is where you give the details in your implementation. Talk
about specific software packages you used, hardware modules, any algorithms or
research papers you referred to, data structure and protocol choices, etc. You should
provide at least an informal list of citations of all these external materials that went into
your project."


## Results

todo: "So, how did things turn out? You can provide performance results, experiences
you had interacting with it, etc. Also talk about what the takeaway is - why should we
care about your results? And, it is ok for things to go wrong - what did not go right in your
project, what was hard and what lessons did you learn?"


## Demo Videos

We recommend watching these videos on a large screen and/or setting your video player to HD/1080p.

todo: Record demo videos (we both need to contribute)

Ideas

* Eric?: Demo sensor HW and bring up (talk through HW design and demo hello.py)
* Eric? (prettier sensors): Demo sensor installation and connection to the server (talk through sensor LED transitions and show server and data logs)
* Devin?: Demo website with live and historical data


## Project Repository

https://github.com/EricSchrock/co2-monitor


## What We Learned

### Eric

todo: Add a paragraph on things learned. Compare to the things you expected to learn in the project proposal.

Ideas

* Using Python for Embedded applications
* Refresher after years without soldering
* Networking via the Python sockets lib
* Web development using Flask
* Using the Raspberry Pi Pico WH


### Devin

todo: Add a paragraph on things learned. Compare to the things you expected to learn in the project proposal.


## Conclusion

In conclusion, we accomplished the high level goal of our project, to prototype a distributed, networked, and affordable CO2 monitoring solution. Along the way, we tried new technologies, built new skills, and gained a deeper understanding of the quality of the air in our homes and of how it impacts our health.
