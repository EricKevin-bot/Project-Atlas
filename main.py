from agents.ceo_agent import CEOAgent


def main() -> None:
    ceo = CEOAgent()
    ceo.morning_briefing()
    ceo.run_company()


if __name__ == "__main__":
    main()