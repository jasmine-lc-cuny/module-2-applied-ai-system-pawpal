# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The three core actions I wanted PawPal+ to support were adding a pet, scheduling care tasks like walks or medication, and viewing a sorted daily schedule. My initial UML design used four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. `Owner` stores multiple pets, `Pet` stores pet details and its task list, `Task` represents one care activity, and `Scheduler` acts as the organizer that sorts, filters, completes, and checks tasks. I kept the design simple so the Streamlit UI could call clear backend methods instead of mixing scheduling logic into the page.

**b. Design changes**

During the initial design pass, I added `due_date`, `frequency`, and `completed` directly to `Task` because recurring tasks and completion status are central to the assignment. I also made `Scheduler` depend on `Owner` instead of storing its own separate task list, because the owner already connects all pets and tasks. This avoids duplicated data and makes the relationships easier to reason about.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
