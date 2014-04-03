## Master Branch
We consider <code>origin/master</code> to be the main branch where the source code of HEAD always reflects a production-ready state. Thus, the master branch should always compile and run successfully, even if unimplemented functions/sections must be stubbed out or unimplemented to achieve this. 

## Development Branch
We consider <code>origin/develop</code> to be the main branch where the source code of HEAD always reflects a state with the latest delivered development changes that will go into the next release/version number.  Should we choose to, for example, implement continuous integration using [Travis](https://travis-ci.org/‎), this would be where where automatic builds would be built from. 

When the source code in <code>develop</code> reaches a stable point and is ready to be released, all of the changes should be merged back into master and then tagged with a release number. 

## Supporting Branches
Next to the main branches <code>master</code> and <code>develop</code>, we use supporting branches to aid parallel development between team members, ease tracking of features, prepare for releases and to assist in quickly fixing serious problems. Unlike the main branches, these branches always have a limited life time, since they will be removed eventually.

A larger project may separate supporting branches into categories including feature branches, release branches, and hotfix branches, however given the smaller scale of splatfilch this is likely not necessary.  

Developers are encouraged to create new branches on a per-feature, per-bug, or per-release basis, and while as a *general* rule, supporting branches should branch from and merge to <code>origin/develop</code>, this rule is in no way enforced. 

## Visual Guide
This illustration is more complex than the simplified strategy outlined above but fits the overall functionality. 
![got heem](http://nvie.com/img/2009/12/Screen-shot-2009-12-24-at-11.32.03.png "yep")
Thanks to [Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/) for this great image.
