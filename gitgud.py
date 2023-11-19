import git

def get_merge_stats(repo_path):
    repo = git.Repo(repo_path)

    # Dictionary to store commit statistics for each user
    user_stats = {}

    for commit in repo.iter_commits('--all'):
        author_name = commit.author.name

        # If the author is not in the dictionary, initialize their stats
        if author_name not in user_stats:
            user_stats[author_name] = {'total_commits': 0, 'merge_commits': 0}

        # Update total commits and count merge master commits
        user_stats[author_name]['total_commits'] += 1
        if commit.message.lower().startswith('merge branch '):
            user_stats[author_name]['merge_commits'] += 1

    return user_stats

def main():
    repo_path = input("Please enter the path to your local git repo\n")  # Replace with the path to your Git repository
    user_stats = get_merge_stats(repo_path)

    # Sort user_stats by the percentage of merge master commits in descending order
    sorted_user_stats = sorted(user_stats.items(), key=lambda x: (x[1]['merge_commits'] / x[1]['total_commits']), reverse=True)

    # Print the results
    print("User\tTotal Commits\tMerge Commits\tPercentage of Merge Commits")
    print("-" * 80)
    
    for user, stats in sorted_user_stats:
        total_commits = stats['total_commits']
        merge_commits = stats['merge_commits']
        percentage = (merge_commits / total_commits) * 100 if total_commits > 0 else 0

        print(f"{user}\t{total_commits}\t\t{merge_commits}\t\t\t{percentage:.2f}%")

if __name__ == "__main__":
    main()
