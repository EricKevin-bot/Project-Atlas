class RetryManager:
    def retry(self, review, content, pipeline):
        recommendation = review.recommendation

        print(f"\n🔄 Retry Manager: {recommendation}")

        if recommendation == "regenerate_title":
            pipeline.title_agent.run(content)

        elif recommendation == "rewrite_script":
            pipeline.script_agent.run(content)

        elif recommendation == "improve_description":
            pipeline.description_agent.run(content)

        elif recommendation == "improve_tags":
            pipeline.tags_agent.run(content)

        elif recommendation == "regenerate_research":
            pipeline.research_agent.run(content)

        else:
            print("No retry action available.")
            return content

        print("Running quality review again...")

        content.review = pipeline.quality_agent.run(content)

        return content