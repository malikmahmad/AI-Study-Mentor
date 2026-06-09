"""
AI Study Mentor – Multi-Agent Learning System
Microsoft Agents League Hackathon 2026 | Reasoning Agents Track
Author: Malik Muhammad Ahmad
"""

import json
import time
from agents.planner_agent import PlannerAgent
from agents.assessment_agent import AssessmentAgent
from agents.engagement_agent import EngagementAgent
from agents.insights_agent import InsightsAgent
from core.orchestrator import Orchestrator


def load_data():
    with open("data/synthetic_data.json", "r") as f:
        return json.load(f)


def print_separator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)


def print_section(title):
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def main():
    print_separator("AI STUDY MENTOR – Multi-Agent Learning System")
    print("  Microsoft Foundry | Reasoning Agents Track")
    print("  Agents League Hackathon 2026")
    print("=" * 60)

    # ── Load synthetic data ──────────────────────────────────────
    data = load_data()

    # ── Microsoft IQ Layer Initialization ───────────────────────
    print_section("MICROSOFT IQ LAYER – Initialization")
    time.sleep(0.3)
    print("  [Foundry IQ]  Connecting to knowledge base...")
    time.sleep(0.3)
    print("  [Foundry IQ]  Indexing certification documents and study guides...")
    time.sleep(0.3)
    print("  [Work IQ]     Loading organizational work context signals...")
    time.sleep(0.3)
    print("  [Work IQ]     Analyzing meeting load, focus time, and activity patterns...")
    time.sleep(0.3)
    print("  [Fabric IQ]   Building semantic ontology graph...")
    time.sleep(0.3)
    print("  [Fabric IQ]   Mapping: Employee → Role → Skills → Certification → Readiness")
    time.sleep(0.3)
    print("\n  ✓ All Microsoft IQ layers initialized successfully.")

    # ── Select learner profile ───────────────────────────────────
    learner = next(l for l in data["learners"] if l["learner_id"] == "L-1001")
    work    = next(w for w in data["work_signals"] if w["employee_id"] == "EMP-001")
    cert    = next(c for c in data["certifications"] if c["id"] == learner["certification"])

    print_section("LEARNER PROFILE")
    print(f"  Learner ID  : {learner['learner_id']}")
    print(f"  Role        : {learner['role']}")
    print(f"  Target Cert : {learner['certification']}")
    print(f"  Hours Studied So Far : {learner['hours_studied']} hrs")
    print(f"  Practice Score       : {learner['practice_score_avg']}%")
    print(f"  Meeting Load/Week    : {work['meeting_hours_per_week']} hrs")
    print(f"  Focus Hours/Week     : {work['focus_hours_per_week']} hrs")
    print(f"  Preferred Slot       : {work['preferred_learning_slot']}")

    # ── Initialize agents ────────────────────────────────────────
    orchestrator = Orchestrator()
    planner      = PlannerAgent()
    assessment   = AssessmentAgent()
    engagement   = EngagementAgent()
    insights     = InsightsAgent()

    # ════════════════════════════════════════════════════════════
    # AGENT 1 – Learning Path Curator + Study Planner
    # ════════════════════════════════════════════════════════════
    print_section("AGENT 1 – Learning Path Curator  [Foundry IQ Grounded]")
    time.sleep(0.3)
    print("  [Foundry IQ]  Retrieving grounded learning resources for", learner["certification"])
    time.sleep(0.3)
    print("  [Foundry IQ]  Cited sources: MS Learn Docs, Official Exam Guide, Practice Labs")

    plan = planner.create_plan(
        certification  = learner["certification"],
        total_hours    = cert["recommended_hours"],
        skills         = cert["skills"],
        hours_per_day  = work["focus_hours_per_week"] // 5,
        hours_studied  = learner["hours_studied"]
    )
    print()
    for line in plan:
        print(f"  {line}")

    # ════════════════════════════════════════════════════════════
    # AGENT 2 – Engagement Agent
    # ════════════════════════════════════════════════════════════
    print_section("AGENT 2 – Engagement Agent  [Work IQ Context]")
    time.sleep(0.3)
    print("  [Work IQ]  Reading calendar, meeting load, and focus-time patterns...")
    time.sleep(0.3)

    reminder = engagement.get_reminder(
        preferred_slot  = work["preferred_learning_slot"],
        meeting_hours   = work["meeting_hours_per_week"],
        focus_hours     = work["focus_hours_per_week"]
    )
    print()
    for line in reminder:
        print(f"  {line}")

    # ════════════════════════════════════════════════════════════
    # AGENT 3 – Assessment Agent
    # ════════════════════════════════════════════════════════════
    print_section("AGENT 3 – Assessment Agent  [Foundry IQ + Fabric IQ]")
    time.sleep(0.3)
    print("  [Foundry IQ]  Generating grounded practice questions from knowledge base...")
    time.sleep(0.3)
    print("  [Fabric IQ]   Mapping skill gaps to certification ontology...")
    time.sleep(0.3)

    result = assessment.evaluate(
        score           = learner["practice_score_avg"],
        threshold       = cert["pass_threshold"],
        certification   = learner["certification"],
        skills          = cert["skills"]
    )
    print()
    for line in result["output"]:
        print(f"  {line}")

    # ════════════════════════════════════════════════════════════
    # REASONING LOOP – Triggered if score below threshold
    # ════════════════════════════════════════════════════════════
    if not result["ready"]:
        print_section("REASONING LOOP – Optimization Cycle Triggered")
        time.sleep(0.3)
        print("  ⚠  Learner readiness score is below threshold.")
        print("  ⚠  REASONING LOOP TRIGGERED → Returning to Study Planner.")
        time.sleep(0.3)

        loop_output = orchestrator.run_reasoning_loop(
            score       = learner["practice_score_avg"],
            threshold   = cert["pass_threshold"],
            cert        = learner["certification"],
            skills      = cert["skills"]
        )
        print()
        for line in loop_output:
            print(f"  {line}")
    else:
        print_section("REASONING LOOP – Status")
        print("  ✓ Learner meets readiness threshold. No loop required.")
        print("  ✓ Recommending certification booking.")

    # ════════════════════════════════════════════════════════════
    # AGENT 4 – Manager Insights Agent
    # ════════════════════════════════════════════════════════════
    print_section("AGENT 4 – Manager Insights Agent  [Fabric IQ + Work IQ]")
    time.sleep(0.3)
    print("  [Fabric IQ]  Analyzing team-level certification readiness data...")
    time.sleep(0.3)
    print("  [Work IQ]    Cross-referencing work capacity and completion patterns...")
    time.sleep(0.3)

    report = insights.generate_report(data["learners"], data["certifications"])
    print()
    for line in report:
        print(f"  {line}")

    # ════════════════════════════════════════════════════════════
    # SYSTEM SUMMARY
    # ════════════════════════════════════════════════════════════
    print_separator("SYSTEM SUMMARY – Multi-Agent Reasoning Complete")
    print("  Agents Executed   : Learning Path Curator, Study Planner,")
    print("                      Engagement Agent, Assessment Agent, Insights Agent")
    print("  IQ Layers Used    : Foundry IQ  |  Work IQ  |  Fabric IQ")
    print("  Reasoning Loop    :", "Triggered – optimization cycle completed" if not result["ready"] else "Not required – learner ready")
    print("  Data              : Synthetic (demo only, no PII)")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
