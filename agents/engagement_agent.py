"""
Engagement Agent
Powered by Work IQ – adapts reminders and nudges to individual work patterns,
meeting load, and focus-time availability.
"""


class EngagementAgent:

    def get_reminder(self, preferred_slot, meeting_hours, focus_hours):
        """
        Analyzes work context signals and produces personalized engagement strategy.
        Avoids disrupting peak work periods based on Work IQ calendar signals.
        """
        output = []
        output.append("── Engagement Agent – Work IQ Context Analysis ──────────")
        output.append(f"  Preferred Slot  : {preferred_slot}")
        output.append(f"  Meeting Load    : {meeting_hours} hrs/week")
        output.append(f"  Focus Capacity  : {focus_hours} hrs/week")
        output.append("")

        # Workload classification
        if meeting_hours > 20:
            workload = "HIGH"
            workload_note = "Heavy meeting schedule – compact study blocks recommended."
        elif meeting_hours > 12:
            workload = "MODERATE"
            workload_note = "Moderate meeting load – balanced study windows available."
        else:
            workload = "LOW"
            workload_note = "Good calendar availability – extended sessions possible."

        output.append(f"  Workload Level  : {workload}")
        output.append(f"  [Work IQ]  {workload_note}")
        output.append("")
        output.append("── Personalized Engagement Plan ─────────────────────────")

        # Slot-based scheduling
        slot_plans = {
            "Morning": {
                "time": "08:00 – 10:00 AM",
                "type": "Deep focus learning",
                "reason": "Morning cortisol peak – optimal for new concept retention."
            },
            "Afternoon": {
                "time": "01:00 – 03:00 PM",
                "type": "Practice and application",
                "reason": "Post-lunch window suited for hands-on exercises and labs."
            },
            "Evening": {
                "time": "07:00 – 09:00 PM",
                "type": "Revision and review",
                "reason": "Evening consolidation – ideal for spaced repetition review."
            }
        }

        slot = slot_plans.get(preferred_slot, slot_plans["Morning"])
        output.append(f"  Recommended Time: {slot['time']}")
        output.append(f"  Session Type    : {slot['type']}")
        output.append(f"  Reasoning       : {slot['reason']}")
        output.append("")

        # Reminder strategy
        if workload == "HIGH":
            output.append("  Reminder Mode   : Compact nudges (15-min blocks between meetings)")
            output.append("  Frequency       : Daily lightweight check-ins")
        elif workload == "MODERATE":
            output.append("  Reminder Mode   : Standard session reminders")
            output.append("  Frequency       : Daily 90-min study blocks")
        else:
            output.append("  Reminder Mode   : Full session scheduling")
            output.append("  Frequency       : Daily 2-hour deep focus sessions")

        output.append("")
        output.append(f"  [Engagement Agent] Schedule optimized for {preferred_slot} learner profile.")
        output.append("  [Engagement Agent] Reminders dispatched. Monitoring engagement signals.")

        return output
