# Thinking Questions

---

# 1. How should the AI handle guest complaints differently from pre-sales inquiries?

Guest complaints should be handled with a much higher level of caution, empathy, and operational oversight compared to pre-sales inquiries.

Pre-sales inquiries such as pricing or availability are generally structured, objective, and lower-risk. These types of questions are usually safe for automated handling because the answers are predictable and based on known property information.

Complaints are fundamentally different because they often involve:

- emotional frustration
- operational failures
- refund requests
- reputational risk
- urgent guest dissatisfaction

Because of this, the system should avoid fully autonomous handling of complaints.

In this project, complaint-related messages intentionally receive:

- lower confidence scores
- automatic escalation behavior
- empathetic response tone
- human review preference

The AI is instructed to acknowledge frustration professionally while avoiding promises related to refunds, compensation, or operational guarantees.

This approach helps balance automation efficiency with guest trust and operational safety.

---

# 2. If a guest says “The AC is not working” at 2 AM, what should happen operationally?

Operationally, this should trigger a high-priority escalation workflow rather than a normal automated response flow.

The ideal workflow would include:

1. Immediate acknowledgment to the guest
2. Automatic escalation classification
3. Notification to the on-call support or operations team
4. Creation of an urgent maintenance task
5. Tracking until resolution

Even if AI generates the initial response, human operational involvement becomes critical in situations involving:

- guest comfort
- safety
- active stay disruption
- potential refund scenarios

In a production system, this workflow could integrate with:

- SMS alerts
- WhatsApp escalation
- maintenance dashboards
- incident tracking systems
- priority support queues

The AI should primarily act as an operational assistant that accelerates response coordination rather than replacing human intervention entirely during urgent incidents.

---

# 3. What additional AI-powered features would improve the platform in the future?

Several AI-powered features could significantly improve both operational efficiency and guest experience over time.

One valuable improvement would be sentiment analysis for detecting frustration, urgency, or dissatisfaction patterns automatically. This would allow the system to proactively escalate risky guest interactions earlier.

Another improvement would be predictive maintenance intelligence. For example, if multiple guests repeatedly mention issues such as weak WiFi, AC problems, or water pressure concerns, the system could identify recurring operational failures before they become widespread problems.

Additional future enhancements could include:

- multilingual guest support
- AI-powered conversation summaries
- automated task generation
- personalized guest recommendations
- CRM integration
- smart escalation prioritization
- property performance analytics
- conversation memory across channels

Long-term, the platform could evolve from a messaging assistant into a broader hospitality operations intelligence system that helps teams improve both guest satisfaction and operational efficiency.