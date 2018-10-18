# .net Dependency Check Suppression

This repo contains false positive suppressions for standard .net libraries from NuGet.

It's for use with [OWASP Dependency Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) - [GitHub project here](https://github.com/jeremylong/DependencyCheck).

I wanted a standard "global" suppression file for my build pipelines that contains all the packages I use from NuGet that have false positives. And I don't want to maintain it per project.

