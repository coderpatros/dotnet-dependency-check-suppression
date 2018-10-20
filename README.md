# .net Dependency Check Suppression

## Overview
This repo contains false positive suppressions for .net libraries from NuGet.

It's for use with [OWASP Dependency Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) - [GitHub project here](https://github.com/jeremylong/DependencyCheck).

I wanted a standard "global" suppression file for my build pipelines that contains all the packages I use from NuGet that have false positives. And I don't want to maintain it per project.

[patros-identifier-suppression.xml](patros-identifier-suppression.xml) contains a list of suppression rules for false positive identifiers  
[patros-vulnerability-suppression.xml](patros-vulnerability-suppression.xml) contains a list of suppression rules for false positive vulnerabilities

To combine the files into a single file you can use the `combine_suppression_files.py` script (it requires Python 3).

Example usage:

`python combine_suppression_files.py dependency-suppression.xml patros-identifier-suppression.xml patros-vulnerability-suppression.xml`

This creates a file `dependency-suppression.xml` that contains all the rules in `patros-identifier-suppression.xml` and `patros-vulnerability-suppression.xml`.

There isn't anything too special with the script and if you have your own suppression rules that you would like to add to the mix it should work assuming they use the same xml schema version. Although dependency check supports multiple supression files. I only combine the files in my build pipelines as a convenience.

## Pull Requests

I'm more than happy to take pull requests. Due to the nature of this project I'll need you to provide full details of the package that triggered the false positive. Ideally you'll include the list of packages referenced in your csproj file so I can easily run dependency check myself to reproduce.

If the suppression isn't specific to a particular file version please add a note explaing why the suppression is valid. i.e. "This vuln only applies to msdia.dll" or "This vuln only applies to the VS Code installer."

I'd also ask you to look at how existing rules have been implemented. Particularly around matching filenames carefully if that is what the match needs to be against.

Some examples...

```xml
<filePath regex="true">.*(\/|\\)System\.Threading\.Thread\.dll$</filePath>
```

`(\/|\\)` ensures we have either `/` or `\` as a path separator before `System.Threading.Thread.dll`. And `$` makes sure we are matching on the end of the path.

And...

```xml
<filePath regex="true">^((?!(\/|\\)msdia\.dll$).)*$</filePath>
```

This regex is a bit trickier to pick apart at first glance. But it just uses a negative lookahead to only match file paths that don't end in `/msdia.dll` or `\msdia.dll`. This one is used for a vulnerability which only affects `msdia.dll` but pops up as a false positive against a bunch of standard libraries.
