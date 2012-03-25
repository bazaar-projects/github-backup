github-backup
=============

Backs up all your GitHub repositories.

Usage:

    ./github_backup.py github_user_name ./backup

You can run it as a cron job:

    @hourly /home/user/github_backup.py user /home/user/github_backup

## TODO:

1. Add support for other sites (BitBucket, Google Code etc.)
2. Make it resistant to remote branch deletion or history rewriting
