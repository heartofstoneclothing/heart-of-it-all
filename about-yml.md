# Workflow Syntax for Github Actions

[^1]Workflows
[^2]Events
[^3]Jobs
[^4]Actions
[^5]Runners
[^6]Basics
[^7]Triggers
[^8]Examples
[^9]Syntax
[^10]
[^11]
[^12]
[^13]
[^14]
[^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26]

[^1]: [Workflows][#workflows]

## Workflows

A workflow is a configurable automated process made up of one or more jobs defined within a YAML workflow configuration file. Workflow files must be stored in the `.github/workflows` directory of you repository
  - They can be triggered manually, by an event, at a defined event
  - A repository can have multiple workflows, each of which can perform a different set of tasks such as
    - Building and testing pull requests
    - Deploying your application everytime a release is created
    - Adding a label whenever a new issue is opened

[^2]: [Events][#events]

## Events

An event is a specific activity in a repository that triggers a workflow run

[^3]: [Jobs][#jobs]

## Jobs

A job is a set of steps in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built

[^4]: [Actions][#actions]

## Actions

An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files


[^5]: [Runners][#runners]

## Runners

A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time

[^6]: [Basics][#Basics]

## Basics

A workflow must contain
  - One or more events that trigger the workflow
  - One or more jobs, each of which executes on a runner machine and run on a series of one or more steps
  - Each step can either run scripts or run actions, which are reuseable 

[^7]: [Triggers][#triggers]

## Triggers

Workflow triggers are events that cause a workflow to run. These events can be
  - Events that occur in your workflow's repository
  - Events that occur outside of GitHub and trigger a repository_dispatch event on GitHub
  - Scheduled times
  - Manual

[^8]: [Examples][#examples]

## Examples of Events

- **branch_protection_rule**
  ```yml
  on:
    branch_protection_rule:
      types: [created, deleted]
  ```
- **check_run**
  ```yml
  on:
    check_run:
      types: [requested, completed]
  ```
- **check_suite**
  ```yml
  on:
    check_suite:
      types: [completed]
  ```
- **create**
```yml
on:
  create
```
- **delete**
```yml
on:
  delete
```
- **deployment**
```yml
on:
  deployment
```
- **deployment_status**
```yml
on:
  deployment_status
```
- **discussion**
```yml
on:
  discussion:
    types: [created, edited, answered]
```
- **discussion_comment**
```yml
on:
  discussion_comment:
    types: [created, deleted]
```
- **fork**
```yml
on:
  fork
```
- **gollum**
```yml
on:
  gollum
```
- **issue_comment**
  - issue_comment
```yml
on:
  issue_comment:
    types: [created, deleted]
```
  - issue_comment on issues or pull requests
```yml
on:

jobs:
  pr_commented:
    # This job only runs for pull request comments
    name: PR comment
    if: ${{ github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo A comment on PR $NUMBER
        env:
          NUMBER: ${{ github.event.issue.number }}

  issue_commented:
    # This job only runs for issue comments
    name: Issue comment
    if: {{ !github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo A comment on issue $NUMBER
        env:
          NUMBER: ${{ github.event.issue.number }}
``` 
- **issues**
```yml
on:
  issues:
    types: [opened, edited, milestoned]
```
- **label**
```yml
on:
  label:
    types: [created, deleted]
```
- **merge_group**
```yml
on:
  pull_request:
    branches: ["main"]
  merge_group:
    types: [checks_requested]
```
- **milestone**
```yml
on:
  milestone:
    types: [opened, deleted]
```
- **page_build**
```yml
on:
  page_build
```
- **public**
```yml
on:
  public
```
- **pull_request**
```yml
on:
  pull_request:
    types: [review_requested]
jobs:
  specific_revieww_requested:
    runs-on: ubuntu-latest
    if: ${{ github.event.requested_team.name == 'octo-team' }}
    steps:
      - run: echo 'A review from octo-team was requested'
```
- **pull_request_comment (use issue_comment)**
- **pull_request_review**
  - run a workflow
```yml
on:
  pull_request_review:
    types: [edited, dismissed]
```
  - approved pull_request
```yml
on:
  pull_request_review:
    types: [submitted]

jobs:
  approved:
    if: github.event.review.state == 'approved'
    runs-on: ubuntu-latest
    steps:
      - run: echo "This PR was approved"
```
- **pull_request_review_comment**
```yml
on:
  pull_request_review_comment:
    types: [created, deleted]
```
- **pull_request_target**
  - run a request
```yml
on:
  pull_request_target:
    types: [assigned, opened, synchronize, reopened]
```
- **push**
```yml
on:
  push
```
- **registry_package**
```yml
on:
  registry_package:
    types: [published]
```
- **release**
```yml
on:
  release:
    types: [published]
```
- **repository_dispatch**
```yml
on:
  repository_dispatch:
    types: [test_result]
```
- **schedule**
```yml
on:
  schedule:
    - cron: "15 4,5 * * *"   # <=== Change this value
```
- **status**
```yml
on:
  status
jobs:
  if_error_or_failure:
      runs-on: ubuntu-latest
      if: >-
        gihub.event.state == 'error' ||
        github.event.state == 'failure'
      steps:
        - env:
            DESCRIPTION: ${{  github.event.description }}
        - run: |
            echo The status is error or failed: $DESCRIPTION
```
- **watch**
```yml
on:
  watch:
    types: [started]
```
- **workflow_call**
```yml
on: workflow_call
```
- **workflow_dispatch**
```yml
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'
        required: true
        default: 'warning'
        type: choice
        options:
        - info
        - warning
        - debug
      tags:
        description: 'Test scenario tags'
        required: false
        type: boolean
      environment:
        description: 'Environment to run tests against'
        type: environment
        required: true

jobs:
  log-the-inputs:
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Log level: $LEVEL"
          echo "Tags: $TAGS"
          echo "Environment: $ENVIRONMENT"
        env:
          LEVEL: ${{ inputs.logLevel }}
          TAGS: ${{ inputs.tags }}
          ENVIRONMENT: ${{ inputs.environment }}
```
- **workflow_run**
```yml
on:
  workflow_run:
    workflows: [Build]
    types: [completed]

jobs:
  on-success:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      - run: echo 'The triggering workflow passed'
  on-failure:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    steps:
      - run: echo 'The triggering workflow failed'
```

[^9]: [Syntax][#syntax]

- **name**
- **run-name**
  ```yml
  run-name: Deploy to {{ inputs.deploy_targets }} by {{ github.actor }}
  ```
- **on**
  - single event
  ```yml
  on: push
  ```
  - multiple events
  ```yml
  on: [push, fork]
  ```
  - using activity types
  ```yml
  on:
    label:
      types:
        - created
  ```
  ```yml
  on:
    label:
      types:
        - opened
        - labeled
  ```
  - using filters
  ```yml
  on:
    push:
      branches:
        - main
        - 'releases/**'
  ```
  - using activity types and filters with multiple events
  ```yml
  on:
    label:
      types:
        - created
    push:
      branches:
        - main
    page_build:
  ```
- **on.<event_name>.types**
  ```yml
  on:
    label:
      types: [created,edited]
  ```
- **on.<pull_request|pull_request_target>.<branches|branches-ignore>**
  - including branches
  ```yml
  on:
    pull_request:
      # Sequence of patterns matched against refs/heads
      branches:
        - main
        - 'mona/octocat'
        - 'releases/**'
  ```
  - excluding branches
  ```yml
  on:
    pull_request:
    # Sequence of patterns matched against refs/heads
    branches-ignore:
      - 'mona/octocat'
      - 'releases/**-alpha' 
  ```
  - including and excluding
  ```yml
  on:
    pull_request:
      branches:
         - 'releases/**'
         - '!releases/**-alpha'
  ```
- **on.push.<branches|tags|branches-ignore|tags-ignore>**
  - including branches and tags 
```yml
on:
  push:
    # Sequence of patterns matched against refs/heads
    branches:
      - main
      - 'mona/octocat'
      - 'releases/**'
    # Sequence of patterns matched against refs/tags
    tags:
      - v2
      - v1.*
```
  - including and excluding branches and tags
```yml
on:
  push:
    branches:
      - 'releases/**'
      - '!releases/**-alpha'
```
- **on.<push|pull_request|pull_request_target>.<paths|paths-ignore>**
  - including branches and tags
```yml
on:
  push:
      # Sequence of patterns matched against refs/heads
      branches:
        - main
        - 'mona/octocat'
        - 'releases/**'
      # Sequence of patterns matched against refs/tags
      tags:
        - v2
        - v1.*
```
  - excluding branches and tags
```yml
on:
  push:
    # Sequence of patterns matched against refs/heads
    branches-ignore:
      - 'mona/octocat'
      - 'releases/**-alpha'
    # Sequence of patterns matched against refs/tags
    tags-ignore:
      - v2
      - v1.*
```
  - including and excluding branches and tags
```yml
on:
  push:
    branches:
      - 'releases/**'
      - '!releases/**-alpha'
```
- **on.schedule**
  - basic time schedule
```yml
on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '30 5,17 * * *'
```
  - workflow with multiple events
```yml
on:
  schedule:
    - cron: '30 5 * * 1,3'
    - cron: '30 5 * * 2,4'

jobs:
  test_schedule:
    runs-on: ubuntu-latest
    steps:
      - name: Not on Monday or Wednesday
        if: github.event.schedule != '30 5 * * 1,3'
        run: echo "This step will be skipped on Monday and Wednesday"
      - name: Every time
        run: echo "This step will always run"
```
- **on.workflow_call**
- **on.workflow_call.inputs**
```yml
on:
  workflow_call:
    inputs:
      username:
        description: 'A username passed from the caller workflow'
        default: 'john-doe'
        required: false
        type: string

jobs:
  print-username:
    runs-on: ubuntu-latest

    steps:
      - name: Print the input name to STDOUT
        run: echo The username is ${{ inputs.username }}
```
- **on.workflow_call.inputs.<input_id>.type**
- **on.workflow_call.outputs**
```yml
on:
  workflow_call:
    # Map the workflow outputs to job outputs
    outputs:
      workflow_output1:
        description: "The first job output"
        value: ${{ jobs.my_job.outputs.job_output1 }}
      workflow_output2:
        description: "The second job output"
        value: ${{ jobs.my_job.outputs.job_output2 }}
```
- **on.workflow_call.secrets**
```yml
on:
  workflow_call:
    secrets:
      access-token:
        description: 'A token passed from the caller workflow'
        required: false

jobs:

  pass-secret-to-action:
    runs-on: ubuntu-latest
    steps:
    # passing the secret to an action
      - nam: Pass the received secret to an action
        uses: ./.github/actions/my-action
        with: ${{ secrets.access-token }}

  # passing the secret to a nested reusable workflow
  pass-secret-to-workflow:
    uses: ./.github/workflows/my-workflow
    secrets:
      token: ${{ secrets.access-token }}
```
- **on.workflow_call.secrets.<secret_id>**
- **on.workflow_call.secrets.<secret_id>.required**
- **on.workflow_run.<branches|branches-ignore>**
  - runs on releases
```yml
on:
  workflow_run:
    workflows: ["Build"]
    types: [requested]
    branches:
      - 'releases/**'
```
  - runs on build
```yml
on:
  workflow_run:
    workflows: ["Build"]
    types: [requested]
    branches-ignore:
      - "canary"
```
  - build runs on branch
```yml
on:
  workflow_run:
    workflows: ["Build"]
    types: [requested]
    branches:
      - 'releases/**'
      - '!releases/**-alpha'
```
- **on.workflow_dispatch**
- **on.workflow_dispatch.inputs**
```yml
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'
        required: true
        default: 'warning'
        type: choice
        options:
          - info
          - warning
          - debug
      print_tags:
        description: 'True to print to STDOUT'
        required: true
        type: boolean
      tags:
        description: 'Test scenario tags'
        required: true
        type: string
      environment:
        description: 'Environment to run tests against'
        type: environment
        required: true

jobs:
  print-tag:
    runs-on: ubuntu-latest
    if:  ${{ inputs.print_tags }} 
    steps:
      - name: Print the input tag to STDOUT
        run: echo  The tags are ${{ inputs.tags }}
```
- **on.workflow_dispatch.inputs.<input_id>.required**
- **on.workflow_dispatch.inputs.<input_id>.type**
- **permissions**
```yml
permissions:
  actions: read|write|none
  attestations: read|write|none
  checks: read|write|none
  contents: read|write|none
  deployments: read|write|none
  id-token: write|none
  issues: read|write|none
  discussions: read|write|none
  packages: read|write|none
  pages: read|write|none
  pull-requests: read|write|none
  repository-projects: read|write|none
  security-events: read|write|none
  statuses: read|write|none
```
- **env**
 ```yml
env:
  SERVER: production
```
- **defaults**
- **defaults.run**
 ```yml
defaults:
  run:
    shell: bash
    working-directory: ./scripts
```
- **defaults.run.shell**
- **defaults.run.working-directory**
- **concurrency**
  - runs specifically on a branch
```yml
on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
  - limit jobs
```yml
on:
  push:
    branches:
      - main

jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: example-group
      cancel-in-progress: true
```
  - staging
```yml
jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: staging_environment
      cancel-in-progress: true
```
  - dynamic
```yml
on:
  push:
    branches:
      - main

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```
  - cancel in-progress job or run
```yml
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true
```
  - fallback value
```yml
concurrency:
  group: ${{ github.head_ref || github.run_id }}
  cancel-in-progress: true
```
  - cancel in-progress or run current
```yml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
  - cancel in-progress on branch
```yml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !contains(github.ref, 'release/')}}
```
- **jobs**
- **jobs.<job_id>**
```yml
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```
- **jobs.<job_id>.name**
- **jobs.<job_id>.permissions**
- **jobs.<job_id>.needs**
```yml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    if: ${{ always() }}
    needs: [job1, job2]
```
- **jobs.<job_id>.if**
  - basic
```yml
if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
```
  - on repo
```yml
name: example-workflow
on: [push]
jobs:
  production-deploy:
    if: github.repository == 'octo-org/octo-repo-prod'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
```
- **jobs.<job_id>.runs-on**
  - basic
```yml
runs-on: [self-hosted, linux, x64, gpu]
```
- mix strings and variables
```yml
on:
  workflow_dispatch:
    inputs:
      chosen-os:
        required: true
        type: choice
        options:
        - Ubuntu
        - macOS

jobs:
  test:
    runs-on: [self-hosted, "${{ inputs.chosen-os }}"]
    steps:
    - run: echo Hello world!
```
- operating system
```yml
runs-on: ubuntu-latest
```
- choose runners
```yml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: 
      group: ubuntu-runners
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```
- groups and labels
```yml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      group: ubuntu-runners
      labels: ubuntu-20.04-16core
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```
- **jobs.<job_id>.environment**
  - single environment
```yml
environment: staging_environment
```
  - using url
```yml
environment:
  name: production_environment
  url: https://github.com
```
  - using output as url
```yml
environment:
  name: production_environment
  url: ${{ steps.step_id.outputs.url_output }}
```
  - using an expression
```yml
environment:
  name: ${{ github.ref_name }}
```
- **jobs.<job_id>.concurrency**
  - using default
```yml
on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
  - at job level
```yml
on:
  push:
    branches:
      - main

jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: example-group
      cancel-in-progress: true
```
  - groups
```yml
jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: staging_environment
      cancel-in-progress: true
```
  - dynamic
```yml
on:
  push:
    branches:
      - main

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```
  - cancel in-progress
```yml
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true
```
  - using fallback
```yml
concurrency:
  group: ${{ github.head_ref || github.run_id }}
  cancel-in-progress: true
```
  - cancel in-progress on specified
```yml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !contains(github.ref, 'release/')}}
```
- **jobs.<job_id>.outputs**
  - defining outputs
```yml
jobs:
  job1:
    runs-on: ubuntu-latest
    # Map a step output to a job output
    outputs:
      output1: ${{ steps.step1.outputs.test }}
      output2: ${{ steps.step2.outputs.test }}
    steps:
      - id: step1
        run: echo "test=hello" >> "$GITHUB_OUTPUT"
      - id: step2
        run: echo "test=world" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - env:
          OUTPUT1: ${{needs.job1.outputs.output1}}
          OUTPUT2: ${{needs.job1.outputs.output2}}
        run: echo "$OUTPUT1 $OUTPUT2"
```
  - outputs in a matrix
```yml
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output_1: ${{ steps.gen_output.outputs.output_1 }}
      output_2: ${{ steps.gen_output.outputs.output_2 }}
      output_3: ${{ steps.gen_output.outputs.output_3 }}
    strategy:
      matrix:
        version: [1, 2, 3]
    steps:
      - name: Generate output
        id: gen_output
        run: |
          version="${{ matrix.version }}"
          echo "output_${version}=${version}" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: [job1]
    steps:
      # Will show
      # {
      #   "output_1": "1",
      #   "output_2": "2",
      #   "output_3": "3"
      # }
      - run: echo '${{ toJSON(needs.job1.outputs) }}'
```
- **jobs.<job_id>.env**
```yml
jobs:
  job1:
    env:
      FIRST_NAME: Mona
```
- **jobs.<job_id>.defaults**
- **jobs.<job_id>.defaults.run**
- **jobs.<job_id>.defaults.run.shell**
- **jobs.<job_id>.defaults.run.working-directory**
```yml
jobs:
  job1:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: ./scripts
```
- **jobs.<job_id>.steps**
```yml
name: Greeting from Mona

on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        env:
          MY_VAR: Hi there! My name is
          FIRST_NAME: Mona
          MIDDLE_NAME: The
          LAST_NAME: Octocat
        run: |
          echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```
- **jobs.<job_id>.steps[*].id**
- **jobs.<job_id>.steps[*].if**
  - basic
```yml
if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
```
  - using contexts
```yml
steps:
  - name: My first step
    if: ${{ github.event_name == 'pull_request' && github.event.action == 'unassigned' }}
    run: echo This event is a pull request that had an assignee removed.
```
  - using status check
```yml
steps:
  - name: My first step
    uses: octo-org/action-name@main
  - name: My backup step
    if: ${{ failure() }}
    uses: actions/heroku@1.0.0
```
  - using secrets
```yml
name: Run a step if a secret has been set
on: push
jobs:
  my-jobname:
    runs-on: ubuntu-latest
    env:
      super_secret: ${{ secrets.SuperSecret }}
    steps:
      - if: ${{ env.super_secret != '' }}
        run: echo 'This step will only run if the secret has a value set.'
      - if: ${{ env.super_secret == '' }}
        run: echo 'This step will only run if the secret does not have a value set.'
```
- **jobs.<job_id>.steps[*].name**
- **jobs.<job_id>.steps[*].uses**
  - versioned actions
```yml
steps:
  # Reference a specific commit
  - uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3
  # Reference the major version of a release
  - uses: actions/checkout@v4
  # Reference a specific version
  - uses: actions/checkout@v4.2.0
  # Reference a branch
  - uses: actions/checkout@main
```
  - public action
```yml
jobs:
  my_first_job:
    steps:
      - name: My first step
        # Uses the default branch of a public repository
        uses: actions/heroku@main
      - name: My second step
        # Uses a specific version tag of a public repository
        uses: actions/aws@v2.0.1
```
  - public action in subdirectory
```yml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/aws/ec2@main
```
  - action in same repo
```yml
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v4
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action
```
- **jobs.<job_id>.steps[*].run**
  - single
```yml

```
  - multi-line
```yml

```
- **jobs.<job_id>.steps[*].working-directory**
```yml

```
- **jobs.<job_id>.steps[*].shell**
  - bash
```yml
steps:
  - name: Display the path
    shell: bash
    run: echo $PATH
```
  - windows
```yml
steps:
  - name: Display the path
    shell: cmd
    run: echo %PATH%
```
  - powershell
```yml
steps:
  - name: Display the path
    shell: pwsh
    run: echo ${env:PATH}
```
  - powershell desktop
```yml
steps:
  - name: Display the path
    shell: powershell
    run: echo ${env:PATH}
```
  - python
```yml
steps:
  - name: Display the path
    shell: python
    run: |
      import os
      print(os.environ['PATH'])
```
  - custom
```yml
steps:
  - name: Display the environment variables and their values
    shell: perl {0}
    run: |
      print %ENV
```
- **jobs.<job_id>.steps[*].with**
```yml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/hello_world@main
        with:
          first_name: Mona
          middle_name: The
          last_name: Octocat
```
- **jobs.<job_id>.steps[*].with.args**
```yml
steps:
  - name: Explain why this job ran
    uses: octo-org/action-name@main
    with:
      entrypoint: /bin/echo
      args: The ${{ github.event_name }} event triggered this step.
```
- **jobs.<job_id>.steps[*].with.entrypoint**
```yml
steps:
  - name: Run a custom command
    uses: octo-org/action-name@main
    with:
      entrypoint: /a/different/executable
```
- **jobs.<job_id>.steps[*].env**
```yml
steps:
  - name: My first action
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      FIRST_NAME: Mona
      LAST_NAME: Octocat
```
- **jobs.<job_id>.steps[*].continue-on-error**
- **jobs.<job_id>.steps[*].timeout-minutes**
- **jobs.<job_id>.timeout-minutes**
- **jobs.<job_id>.strategy**
- **jobs.<job_id>.strategy.matrix**
  - basic
```yml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```
  - single-dimension
```yml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.version }}
```
  - multi-dimension matrix
```yml
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [ubuntu-22.04, ubuntu-20.04]
        version: [10, 12, 14]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.version }}
```
  - array of objects
```yml
matrix:
  os:
    - ubuntu-latest
    - macos-latest
  node:
    - version: 14
    - version: 20
      env: NODE_OPTIONS=--openssl-legacy-provider
```
  - using contexts to create matrices
```yml
{
  "event_type": "test",
  "client_payload": {
    "versions": [12, 14, 16]
  }
}

on:
  repository_dispatch:
    types:
      - test
 
jobs:
  example_matrix:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        version: ${{ github.event.client_payload.versions }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.version }}
```
- **jobs.<job_id>.strategy.matrix.include**
  - example
```yml
strategy:
  matrix:
    fruit: [apple, pear]
    animal: [cat, dog]
    include:
      - color: green
      - color: pink
        animal: cat
      - fruit: apple
        shape: circle
      - fruit: banana
      - fruit: banana
        animal: cat
```
  - expanding configurations
```yml
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        node: [14, 16]
        include:
          - os: windows-latest
            node: 16
            npm: 6
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - if: ${{ matrix.npm }}
        run: npm install -g npm@${{ matrix.npm }}
      - run: npm --version
```
  - adding configurations
```yml
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [macos-latest, windows-latest, ubuntu-latest]
        version: [12, 14, 16]
        include:
          - os: windows-latest
            version: 17
```
  - adding configurations with two jobs
```yml
jobs:
  includes_only:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - site: "production"
            datacenter: "site-a"
          - site: "staging"
            datacenter: "site-b"
```
- **jobs.<job_id>.strategy.matrix.exclude**
```yml
strategy:
  matrix:
    os: [macos-latest, windows-latest]
    version: [12, 14, 16]
    environment: [staging, production]
    exclude:
      - os: macos-latest
        version: 12
        environment: production
      - os: windows-latest
        version: 16
runs-on: ${{ matrix.os }}
```
- **jobs.<job_id>.strategy.fail-fast**
```yml
jobs:
  test:
    runs-on: ubuntu-latest
    continue-on-error: ${{ matrix.experimental }}
    strategy:
      fail-fast: true
      matrix:
        version: [6, 7, 8]
        experimental: [false]
        include:
          - version: 9
            experimental: true
```
- **jobs.<job_id>.strategy.max-parallel**
```yml
jobs:
  example_matrix:
    strategy:
      max-parallel: 2
      matrix:
        version: [10, 12, 14]
        os: [ubuntu-latest, windows-latest]
```
- **jobs.<job_id>.continue-on-error**
```yml
runs-on: ${{ matrix.os }}
continue-on-error: ${{ matrix.experimental }}
strategy:
  fail-fast: false
  matrix:
    node: [13, 14]
    os: [macos-latest, ubuntu-latest]
    experimental: [false]
    include:
      - node: 15
        os: ubuntu-latest
        experimental: true
```
- **jobs.<job_id>.container**
```yml
name: CI
on:
  push:
    branches: [ main ]
jobs:
  container-test-job:
    runs-on: ubuntu-latest
    container:
      image: node:18
      env:
        NODE_ENV: development
      ports:
        - 80
      volumes:
        - my_docker_volume:/volume_mount
      options: --cpus 1
    steps:
      - name: Check for dockerenv file
        run: (ls /.dockerenv && echo Found dockerenv) || (echo No dockerenv)
```
- **jobs.<job_id>.container.image**
- **jobs.<job_id>.container.credentials**
```yml
container:
  image: ghcr.io/owner/image
  credentials:
     username: ${{ github.actor }}
     password: ${{ secrets.github_token }}
```
- **jobs.<job_id>.container.env**
- **jobs.<job_id>.container.ports**
- **jobs.<job_id>.container.volumes**
```yml
volumes:
  - my_docker_volume:/volume_mount
  - /data/my_data
  - /source/directory:/destination/directory
```
- **jobs.<job_id>.container.options**
- **jobs.<job_id>.services**
  - using localhost
```yml
services:
  nginx:
    image: nginx
    # Map port 8080 on the Docker host to port 80 on the nginx container
    ports:
      - 8080:80
  redis:
    image: redis
    # Map random free TCP port on Docker host to port 6379 on redis container
    ports:
      - 6379/tcp
steps:
  - run: |
      echo "Redis available on 127.0.0.1:${{ job.services.redis.ports['6379'] }}"
      echo "Nginx available on 127.0.0.1:${{ job.services.nginx.ports['80'] }}"
```
- **jobs.<job_id>.services.<service_id>.image**
- **jobs.<job_id>.services.<service_id>.credentials**
```yml
services:
  myservice1:
    image: ghcr.io/owner/myservice1
    credentials:
      username: ${{ github.actor }}
      password: ${{ secrets.github_token }}
  myservice2:
    image: dockerhub_org/myservice2
    credentials:
      username: ${{ secrets.DOCKER_USER }}
      password: ${{ secrets.DOCKER_PASSWORD }}
```
- **jobs.<job_id>.services.<service_id>.env**
- **jobs.<job_id>.services.<service_id>.ports**
- **jobs.<job_id>.services.<service_id>.volumes**
```yml
volumes:
  - my_docker_volume:/volume_mount
  - /data/my_data
  - /source/directory:/destination/directory
```
- **jobs.<job_id>.services.<service_id>.options**
- **jobs.<job_id>.uses**
```yml
jobs:
  call-workflow-1-in-local-repo:
    uses: octo-org/this-repo/.github/workflows/workflow-1.yml@172239021f7ba04fe7327647b213799853a9eb89
  call-workflow-2-in-local-repo:
    uses: ./.github/workflows/workflow-2.yml
  call-workflow-in-another-repo:
    uses: octo-org/another-repo/.github/workflows/workflow.yml@v1
```
- **jobs.<job_id>.with**
```yml
jobs:
  call-workflow:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@main
    with:
      username: mona
```
- **jobs.<job_id>.with.<input_id>**
- **jobs.<job_id>.secrets**
```yml
jobs:
  call-workflow:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@main
    secrets:
      access-token: ${{ secrets.PERSONAL_ACCESS_TOKEN }
```
- **jobs.<job_id>.secrets.inherit**
  - option 1
```yml
on:
  workflow_dispatch:

jobs:
  pass-secrets-to-workflow:
    uses: ./.github/workflows/called-workflow.yml
    secrets: inherit
```
  - option two
```yml
on:
  workflow_call:

jobs:
  pass-secret-to-action:
    runs-on: ubuntu-latest
    steps:
      - name: Use a repo or org secret from the calling workflow.
        run: echo ${{ secrets.CALLING_WORKFLOW_SECRET }}
```
- **jobs.<job_id>.secrets.<secret_id>**
