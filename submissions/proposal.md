% **CS 437: Internet of Things** \
  **Final Project Proposal**
---
urlcolor: cyan
---

## Overview

We propose to create a network of CO2 sensors with a web interface. Our goal is
distributed monitoring of indoor air quality.

## Group

One of the motivations of this project is to stretch us beyond what we already know. We have included short professional biographies to illustrate our current skills and how we hope this project extends them.

### Eric Schrock (ejs9)

My Computer Engineering curriculum was a mixture of Electrical Engineering and Computer Science in addition to courses on embedded programming and digital logic design. After graduation, I spent four years in the automotive industry working on advanced driver-assistance systems (ADAS). Devin and I now work together on the root of trust (RoT) for secure servers.

I am most comfortable programming bare metal (no OS) embedded C on microcontrollers. I've also played with various sensors and displays. I have very little experience with networking or web development and I anticipate our project challenging me to grow in these areas.

### Devin Schmitz (devinms3)

My formal Computer Science background consists of only a few introductory
programming courses, algorithms, and data structures, but I have a strong
background in applied mathematics and a broad knowledge of the physical
sciences. My professional experience is all centered around bare metal embedded
C, but I also have a fair knowledge of Linux operating systems and data
analysis with numerical Python. I anticipate most everything else involved in
the project will be a learning opportunity for me. In particular, I have very
little experience with networking and web development, and no experience with
javascript.

## Motivation

Breathing is one of the most fundamental processes of our lives, but most homes
are only equipped with smoke and carbon monoxide detectors, which just warn
against critically dangerous levels of air polution. High levels of pollutants
like Carbon Dioxide (CO2), particulate matter (PM), and volatile organic
compounds (VOCs) can go unnoticed, contributing to drowsiness, illness, and
poor cognitive function, among many other potential poor health
outcomes[^1][^2][^3].

Large pollutants can be filtered out by a good HVAC or air filtration system,
but small asphyxiants such as CO2 and VOCs are best managed with proper air
ventilation. However, the exchange of fresh outdoor air for indoor air works
against the mission of modern HVAC, door, and window systems, which attempt to
maintain a consistent internal climate (in spite of the surrounding
environment) by _avoiding_ the exchange of indoor and outdoor air.

It is easy to open a window during the spring and fall when the weather is
nice, but knowing when it is necessary to open a window for proper air
circulation during the cold winter or hot summer can be a challenge. Having a
window open all the time wastes energy heating excess fresh air, but fatigue
and headache from poor air quality only exacerbates common ailments like
seasonal depression.

The first step to balancing this tension is having data. CO2 serves as a good
proxy for appropriate air ventilation in general. CO2 is a direct byproduct of
respiration and combustion, so indoor levels rise throughout the day as we
breath and use gas appliances like stoves, hot water heaters, and furnaces. By
monitoring indoor CO2 levels, we can have a better idea of when there is
adequate ventilation and when more fresh air exchange is needed.

However, proper air monitoring requires a distributed network. A single sensor,
though useful, does not provide a comprehensive picture of the air quality
throughout a home (especially in homes with poor overall ventilation). A
network of sensors also reduces inaccuracy due to any single faulty sensor
reading and keeps the system more robust to sensor failures. Additionally, many
existing air monitoring solutions are cost prohibitive to deploy across a home,
with individual sensors costing up to $230[^4] and coming with a list of extra
and unnecessary features like onboard data processing and display.

We propose to address these issues by designing simple, low cost, low energy
CO2 sensors that can be deployed throughout a home for real time monitoring of
air quality, with a single central hub for processing and displaying the data
via a convenient web application on the local area network.

[^1]: <https://ehp.niehs.nih.gov/doi/10.1289/ehp.1510037>
[^2]: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4296077>
[^3]: <https://www.niehs.nih.gov/health/topics/agents/air-pollution/index.cfm>
[^4]: <https://www.airthings.com//wave-plus>

\pagebreak

## Timeline

* Since we both lack web and networking experience, we set higher time estimates for related milestones
* "CP" stands for "Checkpoint"

+--------------+-------------------------------------------------+-----------+
| **Week**     | **Milestones**                                  | **Hours** |
+==============+=================================================+===========+
| 6            | - Initial design decisions                      |         4 |
|              | - Parts ordered for initial prototype           |         1 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 7            | - Components individually tested                |         4 |
|              | - Initial prototype built                       |         2 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 8            | - Local display of CO2 readings                 |         3 |
|              | - Test plan showing CO2 level variation         |         1 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| **CP 1**     | **Local CO2 level display**                     |           |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 9            | - Second prototype designed                     |         3 |
|              | - Parts ordered for second prototype            |         1 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 10           | - New components individually tested            |         3 |
|              | - Second prototype assembled and tested         |         2 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 11           | - LAN website displays live CO2 reading         |         5 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| **CP 2**     | **LAN access to live data**                     |           |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 12           | - Website shows historical trends               |         5 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 13           | - Website shows multiple sensors                |         5 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| **CP 3**     | **Fully featured website**                      |           |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 14           | - Design documents updated                      |         2 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| 15           | - Final report and demo video                   |         4 |
+--------------+-------------------------------------------------+-----------+
+--------------+-------------------------------------------------+-----------+
| Hours        |                                                 |        45 |
+--------------+-------------------------------------------------+-----------+
