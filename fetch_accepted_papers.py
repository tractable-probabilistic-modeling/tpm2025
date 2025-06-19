import openreview
import yaml

def fetch_papers_from_openreview(venue_id, output_file):
    """
    Fetches papers from OpenReview for a given venue and writes them to a YAML file.

    :param venue_id: The ID of the venue on OpenReview (e.g., "ICLR.cc/2025/Conference")
    :param output_file: The path to the output YAML file
    """
    client = openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net', username="", password="")

    # Fetch all notes (papers) for the given venue
    venue_group = client.get_group(venue_id)
    print(venue_group)
    submission_name = venue_group.content['submission_name']['value']
    print('===> Submission name')
    print(submission_name)
    #notes = client.get_group(id='auai.org/UAI/2025/Workshop/TPM')
    notes = client.get_all_notes(invitation=f'{venue_id}/-/{submission_name}')
    print(notes)

    papers = []
    for note in notes:
        paper = {
            'title': note.content['title']['value'],
            'authors': ', '.join(note.content['authors']['value']),
        }
        papers.append(paper)

    # Write the papers to a YAML file
    with open(output_file, 'w') as yaml_file:
        yaml.dump(papers, yaml_file, default_flow_style=False, allow_unicode=True)

    print(f"Successfully wrote {len(papers)} papers to {output_file}")

if __name__ == "__main__":
    # Replace with your venue ID and desired output file path
    venue_id = "auai.org/UAI/2025/Workshop/TPM"  # Example venue ID
    output_file = "./_data/papers.yml"  # Adjust the path as needed

    fetch_papers_from_openreview(venue_id, output_file)