<div align="center">
  <img src="assets/portrait-banner.svg" alt="Krishna Chandak: backend developer, with a stylized portrait" width="100%" />

  <p><strong>Backend developer · Python, FastAPI & Django · Pune, India</strong></p>
  <p>Designing reliable APIs, traceable data flows, and systems that make their limits clear.</p>

  <a href="https://www.linkedin.com/in/krishna-chandak04/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
  <a href="mailto:krishnachandak444@gmail.com"><img src="https://img.shields.io/badge/Email-Say%20hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Krishna" /></a>

  <p><sub><a href="#selected-work">Selected work</a> · <a href="#engineering-approach">Engineering approach</a> · <a href="#contributions">Contributions</a> · <a href="#toolkit">Toolkit</a> · <a href="#connect">Connect</a></sub></p>
</div>

---

## About

I'm Krishna, a computer science student at **Pimpri Chinchwad University** and a backend developer who enjoys the parts of software that are easy to overlook: state transitions, retries, data integrity, access control, and the operational path from a working prototype to a dependable service.

My work spans **Python services**, **TypeScript product interfaces**, and experiments where AI assists people without replacing their judgment. In my previous backend internship at **Sarva Suvidhaen Private Limited**, I worked on Django and FastAPI services for railway-related applications, including notification workflows, database performance, access control, and ingestion pipelines.

> **How I work:** define the contract, model the failure path, test the critical behavior, and make the result observable.

## Selected work

<table>
  <tr>
    <td width="50%"><a href="https://github.com/krishnaChandak044/Paypal-AI-hackathon"><img src="assets/cards/reliefrail.svg" alt="ReliefRail: disaster relief coordination prototype" width="100%" /></a></td>
    <td width="50%"><a href="https://github.com/krishnaChandak044/Blackbox-meta-ai-global-hackathon"><img src="assets/cards/blackbox.svg" alt="Blackbox: road incident evidence review prototype" width="100%" /></a></td>
  </tr>
  <tr>
    <td width="50%"><a href="https://github.com/krishnaChandak044/Wallsense"><img src="assets/cards/wallsense.svg" alt="WallSense: recorded Wi-Fi CSI research pipeline" width="100%" /></a></td>
    <td width="50%"><a href="https://github.com/krishnaChandak044/DilCare-Mobile-app"><img src="assets/cards/dilcare.svg" alt="DilCare mobile: React Native health app" width="100%" /></a></td>
  </tr>
</table>

| Project | What makes it interesting | Status |
| :-- | :-- | :-- |
| [**ReliefRail**](https://github.com/krishnaChandak044/Paypal-AI-hackathon) | Models requests, approved needs, pooled contributions, reserves, PayPal Sandbox events, and payout reconciliation as distinct steps. Human coordinators remain in control. | Experimental prototype; Sandbox payments and synthetic demo data. |
| [**Blackbox**](https://github.com/krishnaChandak044/Blackbox-meta-ai-global-hackathon) | Keeps source media, derived analysis, uncertainty, and reviewer decisions separate in a road-incident evidence workspace. | Hackathon prototype; not validated forensic analysis. |
| [**WallSense**](https://github.com/krishnaChandak044/Wallsense) | Validates recorded Wi-Fi CSI datasets and uses recording-safe splits to avoid an easy source of evaluation leakage. | Reproducible baseline and bounded research pilot. |
| [**DilCare mobile**](https://github.com/krishnaChandak044/DilCare-Mobile-app) | Explores health tracking, reminders, and family workflows through a React Native client and API services. | App prototype; health features should not be treated as clinical tools. |

<details>
<summary><strong>Explore the architecture behind the projects</strong></summary>

<br />

- **ReliefRail:** [payment journey, ledger model, and operational boundaries](https://github.com/krishnaChandak044/Paypal-AI-hackathon#how-a-contribution-moves-through-the-system)
- **Blackbox:** [source traceability and review principles](https://github.com/krishnaChandak044/Blackbox-meta-ai-global-hackathon#design-principles)
- **WallSense:** [dataset setup, split rules, and evaluation notes](https://github.com/krishnaChandak044/Wallsense#day-12-setup)
- **DilCare mobile:** [screens, services, and client integration](https://github.com/krishnaChandak044/DilCare-Mobile-app#project-structure)

</details>

## Engineering approach

The most useful technical decisions show up when a system is under stress. These are concrete problems I have explored in public work:

| Failure mode | Design response | Example |
| :-- | :-- | :-- |
| A provider sends the same event twice | Verify and deduplicate the event before changing accounting state. | [ReliefRail](https://github.com/krishnaChandak044/Paypal-AI-hackathon) |
| A payout has an unknown or pending provider state | Keep funds reserved and reconcile before recording spend. | [ReliefRail](https://github.com/krishnaChandak044/Paypal-AI-hackathon) |
| Generated analysis sounds more certain than the evidence | Separate observations, assumptions, simulations, and reviewer conclusions. | [Blackbox](https://github.com/krishnaChandak044/Blackbox-meta-ai-global-hackathon) |
| Train and test rows come from the same recording | Split by recording before training or evaluating a baseline. | [WallSense](https://github.com/krishnaChandak044/Wallsense) |

<details>
<summary><strong>The principles I carry from project to project</strong></summary>

<br />

1. **Make state explicit.** A request, payment, job, or experiment should have a clear lifecycle.
2. **Treat external systems as uncertain.** Timeouts, retries, duplicate events, and partial failures are normal conditions to design for.
3. **Keep evidence traceable.** Preserve the source and label what was measured, inferred, or generated.
4. **Keep people accountable.** AI can draft or assist; sensitive approvals stay reviewable by humans.
5. **Document limitations.** A prototype's useful idea is stronger when its current boundary is stated honestly.

</details>

## Contributions

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/krishnaChandak044/krishnaChandak044/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/krishnaChandak044/krishnaChandak044/output/snake-light.svg" />
    <img src="https://raw.githubusercontent.com/krishnaChandak044/krishnaChandak044/output/snake-light.svg" alt="Animated snake moving through Krishna's GitHub contribution calendar" width="100%" />
  </picture>
  <sub>Contribution snake refreshed twice daily</sub>
</div>

<details>
<summary><strong>View the detailed contribution heatmap</strong></summary>

<br />

<a href="https://github.com/krishnaChandak044?tab=overview"><img src="assets/contributions.svg" alt="Krishna's GitHub contribution heatmap for the past year" width="100%" /></a>

</details>

## Toolkit

<div align="center">
  <p><strong>Backend & data</strong></p>
  <img src="https://skillicons.dev/icons?i=python,fastapi,django,flask,postgres,redis&theme=dark" alt="Python, FastAPI, Django, Flask, PostgreSQL, Redis" />
  <p><strong>Interfaces & delivery</strong></p>
  <img src="https://skillicons.dev/icons?i=ts,react,nextjs,docker,aws,git,githubactions,linux&theme=dark&perline=8" alt="TypeScript, React, Next.js, Docker, AWS, Git, GitHub Actions, Linux" />
</div>

<p align="center"><sub>Also working with REST APIs, SQLAlchemy, Celery, Pytest, React Native, and reproducible data pipelines.</sub></p>

## Community

I have mentored developers with the **AWS DevSecOps User Group Pune**, contributed to the **Microsoft Learn Student Ambassadors PCU** web development team, and participated in **GDG Pune**. I enjoy sharing what I learn and building alongside other developers.

## Connect

Have a backend problem, an open source idea, or a thoughtful technical question? I'd be glad to talk.

<div align="center">
  <a href="https://www.linkedin.com/in/krishna-chandak04/"><img src="https://img.shields.io/badge/Let's%20connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with Krishna on LinkedIn" /></a>
  <a href="mailto:krishnachandak444@gmail.com"><img src="https://img.shields.io/badge/Start%20a%20conversation-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Krishna" /></a>
</div>

<p align="center"><sub>Explore the repositories for implementation details, tests, and each project's current limitations.</sub></p>
