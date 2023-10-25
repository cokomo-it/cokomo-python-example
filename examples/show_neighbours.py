from examples.cokomoapi import print_competence_base_details

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("id")
    args = parser.parse_args()

    print_competence_base_details(id=args.id)