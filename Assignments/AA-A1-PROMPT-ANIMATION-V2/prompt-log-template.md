# Prompt Engineering Log

**Language:** English | [中文版本](prompt-log-template-zh.md)

Complete one copy of the version record for the baseline and for each controlled revision.
Use a minimum of four prompt versions in total.

## Fixed comparison conditions

| Field | Value |
| --- | --- |
| Generation platform |  |
| Model and visible version |  |
| Reference-input method |  |
| Duration |  |
| Aspect ratio and resolution |  |
| Frame rate |  |
| Fixed settings |  |
| Settings the platform does not expose |  |
| Free-tier or quota constraints encountered |  |

## Version record

### Version ID

`V0`, `V1`, `V2`, or later.

### Targeted requirement or diagnosed failure

State the one requirement or failure this version addresses.

### Hypothesis

State the expected effect before generating.

### Exact positive prompt

Paste the prompt verbatim.

### Exact negative prompt

Paste the negative prompt verbatim, or write `Not used`.

### Reference inputs and settings

Record every reference file, reference weight when visible, model setting, seed when available, and other control used for this version.
State whether the service was used through a free tier, free quota, institutional access, or an existing personal subscription; do not include prices or account details.

### Controlled change

Describe exactly what changed from the previous version and what remained fixed.
If the model or service changed, state that explicitly and treat the result as a combined platform-and-prompt change rather than a prompt-only comparison.

### Output evidence

Give the raw output filename and the contact-sheet filename.

### Observations at fixed checkpoints

| Checkpoint | Character placement and action | Sphere contact | Taijitu stability and shading | Anatomy and temporal consistency | Visible artefacts |
| --- | --- | --- | --- | --- | --- |
| 0% |  |  |  |  |  |
| 25% |  |  |  |  |  |
| 50% |  |  |  |  |  |
| 75% |  |  |  |  |  |
| 100% |  |  |  |  |  |

### Comparable scores

Use the same decision rule for every version.

| Score | Anchor |
| ---: | --- |
| 5 | Closely matches the reference requirement; no material defect is visible. |
| 4 | Matches with a minor defect that does not disrupt the scene or action. |
| 3 | Recognisable and mostly correct, but one or more visible defects weaken fidelity. |
| 2 | Major deviation, instability, or artefact disrupts the intended result. |
| 1 | The requirement is absent, incorrect, or unusable. |

| Measure | Score from 1-5 | Evidence for the score |
| --- | ---: | --- |
| Composition and action fidelity |  |  |
| Taijitu geometry, material, and shadow fidelity |  |  |
| Humanoid anatomy and motion harmony |  |  |
| Sphere identity and hand contact |  |  |
| Temporal stability and loop continuity |  |  |

### Evaluation

Did the intervention improve its intended measure?
Did it cause a regression in another measure?
Support the answer with checkpoint evidence rather than an overall impression.

### Diagnosis and next action

Classify the result as a specification failure, reference-use failure, capability or control limitation, or successful intervention.
State the evidence for that diagnosis and the single next change you will test.

---

Duplicate the complete version record for the next prompt version.

## Final supported conclusion

Identify the prompt interventions retained in the final version.
State what your comparisons demonstrate, what remains uncertain, and which visible limitations remain in the submitted animation.
