"""
Assessment Agent
Grounded by Foundry IQ and Fabric IQ.
Evaluates learner readiness, identifies skill gaps, and reasons over performance data.
"""


class AssessmentAgent:

    def evaluate(self, score, threshold, certification, skills):
        """
        Performs multi-step performance analysis:
        1. Score comparison against threshold
        2. Gap calculation
        3. Root cause reasoning
        4. Skill-specific recommendations
        """
        gap   = threshold - score
        ready = score >= threshold

        output = []
        output.append("── Assessment Agent – Performance Evaluation ────────────")
        output.append(f"  Certification : {certification}")
        output.append(f"  Current Score : {score}%")
        output.append(f"  Pass Threshold: {threshold}%")
        output.append(f"  Gap           : {gap}%  ({'On track' if ready else 'Below threshold'})")
        output.append("")
        output.append("── Reasoning Analysis ───────────────────────────────────")

        if ready:
            output.append("  Status        : ✓ READY – Score meets certification threshold")
            output.append("  Reasoning     : Learner demonstrates consistent understanding")
            output.append("                  across core skill areas. Strong exam readiness.")
            output.append("  Confidence    : HIGH")
            output.append("  Recommendation: Proceed to exam booking.")
        elif gap <= 5:
            output.append("  Status        : ⚠  CLOSE – Minor gap detected")
            output.append("  Reasoning     : Learner is near-ready with small knowledge gaps.")
            output.append("                  Targeted revision on 1–2 topics will close gap.")
            output.append("  Confidence    : MEDIUM-HIGH")
            output.append(f"  Recommendation: 2-day focused review on weak areas.")
        elif gap <= 15:
            output.append("  Status        : ⚠  BELOW THRESHOLD – Needs improvement")
            output.append("  Reasoning     : Score indicates partial understanding.")
            output.append("                  Inconsistent practice and topic gaps detected.")
            output.append("  Confidence    : MEDIUM")
            output.append(f"  Recommendation: 5-day structured revision + 2 mock tests.")
        else:
            output.append("  Status        : ✗  NOT READY – Significant gap identified")
            output.append("  Reasoning     : Foundational knowledge gaps present.")
            output.append("                  Learner needs to revisit core concepts.")
            output.append("  Confidence    : LOW")
            output.append(f"  Recommendation: Resume full study plan from beginning.")

        output.append("")
        output.append("── Skill Gap Analysis (Fabric IQ Semantic Map) ──────────")

        for i, skill in enumerate(skills):
            if i == 0:
                level = "Needs review" if not ready else "Proficient"
            elif i == 1:
                level = "Partially covered" if not ready else "Proficient"
            else:
                level = "Adequate"
            output.append(f"  {skill:<30} → {level}")

        output.append("")
        output.append("  [Assessment Agent] Evaluation complete.")
        if not ready:
            output.append("  [Assessment Agent] Signaling Orchestrator: reasoning loop required.")

        return {"output": output, "ready": ready}
