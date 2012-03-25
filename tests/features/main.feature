Feature: Back up GitHub repositories

    Scenario: Fresh backup
        Given an empty directory
        When I back up octocat's repositories
        Then there are 3 subdirectories
        And Hello-World is tracking git://github.com/octocat/Hello-World.git
        And Spoon-Knife is tracking git://github.com/octocat/Spoon-Knife.git
        And ThisIsATest is tracking git://github.com/octocat/ThisIsATest.git

    Scenario: Update
        Given an empty directory
        When I back up octocat's repositories
        When I back up octocat's repositories
        Then there are 3 subdirectories
        And Hello-World is tracking git://github.com/octocat/Hello-World.git
        And Spoon-Knife is tracking git://github.com/octocat/Spoon-Knife.git
        And ThisIsATest is tracking git://github.com/octocat/ThisIsATest.git

    Scenario: Polluted directory
        Given an empty directory
        And a subdirectory Spoon-Knife
        When I back up octocat's repositories
        Then there are 4 subdirectories
        And Hello-World is tracking git://github.com/octocat/Hello-World.git
        And Spoon-Knife is not a Git repository
        And Spoon-Knife_ is tracking git://github.com/octocat/Spoon-Knife.git
        And ThisIsATest is tracking git://github.com/octocat/ThisIsATest.git
        When I back up octocat's repositories
        Then there are 4 subdirectories
        And Spoon-Knife is not a Git repository
        And Spoon-Knife_ is tracking git://github.com/octocat/Spoon-Knife.git

    Scenario: Directory polluted with other repositories
        Given an empty directory
        And a local repository Spoon-Knife
        When I back up octocat's repositories
        Then there are 4 subdirectories
        And Hello-World is tracking git://github.com/octocat/Hello-World.git
        And Spoon-Knife is a Git repository
        And Spoon-Knife_ is tracking git://github.com/octocat/Spoon-Knife.git
        And ThisIsATest is tracking git://github.com/octocat/ThisIsATest.git
        When I back up octocat's repositories
        Then there are 4 subdirectories
        And Spoon-Knife is a Git repository
        And Spoon-Knife_ is tracking git://github.com/octocat/Spoon-Knife.git
