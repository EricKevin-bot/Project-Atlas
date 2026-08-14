import traceback

from agents.ceo_agent import CEOAgent
from config import DEVELOPMENT_MODE


def main() -> None:
    try:
        ceo = CEOAgent()
        ceo.morning_briefing()
        ceo.run_company()

    except KeyboardInterrupt:
        print("\n\n⚠️ Atlas stopped by user.")

    except RuntimeError as error:
        print("\n❌ Atlas could not complete the run.")
        print(f"Reason: {error}")

        if DEVELOPMENT_MODE:
            print("\n🔧 Development traceback:")
            traceback.print_exc()

    except ValueError as error:
        print("\n❌ Atlas received invalid data.")
        print(f"Reason: {error}")

        if DEVELOPMENT_MODE:
            print("\n🔧 Development traceback:")
            traceback.print_exc()

    except Exception as error:
        print("\n❌ Atlas encountered an unexpected error.")
        print(f"Reason: {error}")

        if DEVELOPMENT_MODE:
            print("\n🔧 Development traceback:")
            traceback.print_exc()


if __name__ == "__main__":
    main()