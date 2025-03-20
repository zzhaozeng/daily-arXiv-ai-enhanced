import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="Path to the jsonline file")
    args = parser.parse_args()
    data = []

    with open(args.data, "r") as f:
        for line in f:
            data.append(json.loads(line))

    template = open("paper_template.md", "r").read()
    markdown = "\n\n".join(
        [
            template.format(
                title=item["title"],
                authors=",".join(item["authors"]),
                summary=item["summary"],
                url=item['abs'],
                task=item['AI']['task'],
                motivation=item['AI']['motivation'],
                method=item['AI']['method'],
                result=item['AI']['result'],
                conclusion=item['AI']['conclusion'],
            )
            for item in data
        ]
    )
    with open(args.data.split('_')[0] + '.md', "w") as f:
        f.write(markdown)
