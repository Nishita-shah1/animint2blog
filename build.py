from pathlib import Path

ROOT = Path(__file__).parent


def page(title, description, page_id, root, body, extra_class="", week_nav=False, toc=False):
    css = f"{root}/css/styles.css"
    js = f"{root}/js/site.js"
    icon = f"{root}/assets/favicon.svg"
    week = """
  <div class="week-nav-shell" data-week-nav></div>
""" if week_nav else ""
    if toc:
        inner = f"""
  <div class="page-shell">
    <main class="content">
{body}
    </main>
    <aside class="page-toc" data-page-toc></aside>
  </div>
"""
    else:
        inner = f"""
  <main class="content">
{body}
  </main>
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="{icon}" type="image/svg+xml">
  <link rel="stylesheet" href="{css}">
</head>
<body class="{extra_class}" data-page="{page_id}" data-root="{root}">
{week}{inner}
  <script src="{js}"></script>
</body>
</html>
"""


def week_header(badge, title, dates):
    return f"""
      <header class="week-header">
        <div class="week-badge">{badge}</div>
        <h1 class="week-title">{title}</h1>
        <p class="week-date">{dates}</p>
      </header>
"""


WEEKS = [
    {
        "id": "community-bonding",
        "file": "community-bonding.html",
        "badge": "Community bonding",
        "title": "Polygon holes, origin branches, and the first CI lessons",
        "dates": "2026-05-01 – 2026-05-24",
        "sprint": "Bonding",
        "status": "Complete",
        "prs": "3",
        "issues": "2",
        "home_title": "Polygon holes and origin PRs",
        "progress_when": "Community Bonding · May 1–24",
        "progress_title": "Opened polygon-hole work from the origin repo",
        "progress_status": "PR #326 OPEN · FORK CI FIXED",
        "progress_blurb": "I opened PR #320 for issue #252, then moved the branch onto animint/animint2 as PR #326 after fork secrets blocked coverage jobs. First mentor meeting covered subgroup holes in geom_polygon.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>Community bonding started with work I had already opened in April: support for the <code>subgroup</code> aesthetic in <code>geom_polygon()</code> so polygons with holes render correctly. That matters for isoband contour polygons used in Hi-C genomic visualizations. The first implementation spanned three layers: the R compiler (<code>geom-polygon.r</code>, <code>geom-.r</code>) and the JS renderer (<code>animint.js</code>), using GeoJSON Polygon format with <code>fill-rule: evenodd</code> for transparent holes. I wrote 17 tests covering compiler, renderer, and interactive cases.</p>
      <p>On 7 May I opened <a href="https://github.com/animint/animint2/issues/322">issue #322</a> as my public GSoC log. Toby invited me to the animint developers team and asked that future PRs come from branches in the org, not my fork. He also pointed me at <a href="https://github.com/animint/animint-blog/">animint-blog</a> for write-ups.</p>
      <p>On 11 May I met mentors and other contributors about issue #252. Mid-month I rewrote JavaScript from built-in array methods and <code>forEach</code> loops to <code>d3.nest</code>, matching the rest of animint, and documented the approach. Then CI taught the first hard lesson: on 18–19 May all three checks failed on PR #320 because the PR came from my fork. GitHub blocks repository secrets on fork PRs, so <code>PAT_GITHUB</code> arrived empty and <code>animint2pages</code> tests could not authenticate.</p>
      <p>I pushed the branch to <code>animint/animint2</code> and opened <a href="https://github.com/animint/animint2/pull/326">PR #326</a>. CRAN and R_coverage passed; JS_coverage still failed. On 20 May I closed #320 in favor of #326 and updated the polygon-hole test suite. By 23–24 May I was studying Toby’s draft <a href="https://github.com/animint/animint2/pull/328">PR #328</a>, a stronger failing test for holes, and I adopted a test-first workflow.</p>
      <p>Fork PRs and org-branch PRs are not the same CI environment. Secrets, GitHub Pages helpers, and coverage jobs only work when the branch lives in the origin repository. I also learned that “no display on CI” was the wrong diagnosis: both coverage jobs already use chromote, and some failures are flaky enough to retry. JS_coverage still failed after the secrets fix with Chromote / X server warnings. Renderer tests that open a browser are more thorough than compiler-only tests, but they are also more sensitive to CI setup, so I waited for mentor guidance before changing <code>tests.yaml</code>.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted to port the rendering fix from PR #326 onto the <code>test-polygon-hole</code> branch so the stronger tests in PR #328 pass, then close #326.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/issues/322">Issue #322: GSoC updates</a></li>
        <li><a href="https://github.com/animint/animint2/issues/252">Issue #252: polygon holes</a></li>
        <li><a href="https://github.com/animint/animint2/pull/326">PR #326: origin-branch polygon holes</a></li>
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328: stronger hole tests</a></li>
      </ul>
""",
    },
    {
        "id": "week-1",
        "file": "week-1.html",
        "badge": "Week 1",
        "title": "Test-first polygon holes on PR #328",
        "dates": "2026-05-25 – 2026-05-31",
        "sprint": "Week 1",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Test-first polygon-hole branch",
        "progress_when": "Week 1 · May 25–31",
        "progress_title": "Moved the hole renderer onto a failing test branch",
        "progress_status": "WORKFLOW PIVOT · PR #328",
        "progress_blurb": "Toby asked for a strong failing test first. I ported the subgroup drawing code onto PR #328, cleaned irrelevant binary files from the diff, and committed to this test-first pattern for later PRs.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>Coding week 1 was about changing how I ship the polygon-hole work. Instead of finishing PR #326 and adding tests later, I moved the renderer onto <a href="https://github.com/animint/animint2/pull/328">PR #328</a>, whose tests already failed on master because holes were filled in.</p>
      <p>Toby’s draft branch showed four tooltip failures on master: hovering a hole still found a polygon. With the #326 drawing code, those tests passed locally. The request was explicit: add the renderer to this branch and close #326. More generally, future PRs should start with a strong failing test, then the fix.</p>
      <p>I ported the subgroup rendering fix onto <code>test-polygon-hole</code>. The first port was messy: accidental binary <code>*.r</code> files landed in the diff, and review stalled until I cleaned them out. I learned to copy files from the other branch, then <code>git add</code>, commit, and push, instead of reconstructing the change by hand. After that, the Files changed tab showed only the intended compiler, renderer, and tests.</p>
      <p>A failing test that encodes the hole geometry is stronger than a passing suite that never hovers the empty region. Tooltip opacity at grid points is a precise way to ask “is this pixel inside the polygon?”</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I needed the grid tooltip tests to pass for islands, holes, and filled regions, and to keep the JavaScript aligned with the d3 conventions used in animint.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328: tooltipID helper and hole tests</a></li>
        <li><a href="https://github.com/animint/animint2/pull/326">PR #326: original renderer (later closed)</a></li>
      </ul>
""",
    },
    {
        "id": "week-2",
        "file": "week-2.html",
        "badge": "Week 2",
        "title": "Making the stronger hole tests pass",
        "dates": "2026-06-01 – 2026-06-07",
        "sprint": "Week 2",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Stronger polygon tooltip tests",
        "progress_when": "Week 2 · June 1–7",
        "progress_title": "Debugged the new grid tooltip cases on #328",
        "progress_status": "REVIEW FIXES",
        "progress_blurb": "Most of the week went into PR #328: correcting review comments and finding the renderer logic that makes the grid-based hole tests pass.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>Week 2 stayed on <a href="https://github.com/animint/animint2/pull/328">PR #328</a>. The new tests look for a tooltip at every grid point and expect one only where <code>num=1</code>, the filled polygon, not the hole. On master the grid test failed at 17 of 147 points: holes still reported polygon opacity 0.7. That is the correct red state. My job was to make the SVG path actually punch those holes so hover and click miss the empty interior.</p>
      <p>I worked through remaining review comments, traced why some hole midpoints still produced a tooltip, and kept the renderer on GeoJSON rings plus evenodd fill rather than ad-hoc path strings. Getting the ring winding and d3 path generation right took longer than the R compiler change. Small JS differences produced plots that looked acceptable but still failed tooltip assertions.</p>
      <p>Interactive tests are only as strong as the coordinates they click. A regular grid over the bounding box catches holes that a handful of named points can miss.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted to land the next round of commits on #328 and respond to Toby’s code review on the path builder.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
        <li><a href="https://github.com/animint/animint2/issues/252">Issue #252</a></li>
      </ul>
""",
    },
    {
        "id": "week-3",
        "file": "week-3.html",
        "badge": "Week 3",
        "title": "Review cycles on the hole renderer",
        "dates": "2026-06-08 – 2026-06-14",
        "sprint": "Week 3",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Review cycles on PR #328",
        "progress_when": "Week 3 · June 8–14",
        "progress_title": "Pushed review fixes for polygon holes",
        "progress_status": "COMMITS ON #328",
        "progress_blurb": "I committed renderer updates on PR #328 and then revised them again from Toby’s inline review, keeping the hole tests as the merge bar.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>The visible work this week was a pair of commits on <a href="https://github.com/animint/animint2/pull/328">PR #328</a>: first the hole-path changes, then a follow-up that matched Toby’s comments on the same diff. The PR still mixed a correct idea, holes as GeoJSON rings drawn with evenodd, with JS that was not yet the same as the reviewed code on #326. Review was really about matching that known-good renderer, not inventing a third path builder.</p>
      <p>From 6–9 June I committed the current renderer and tests. On 14 June I updated the same files from inline review. When a mentor says “use the JS from the other PR,” the fastest path is to copy that file, not rewrite the same algorithm in a slightly different style.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I needed to settle the d3 path API, stop chasing Codecov on this PR, and get a locally correct visualization with all hole tests green.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
      </ul>
""",
    },
    {
        "id": "week-4",
        "file": "week-4.html",
        "badge": "Week 4",
        "title": "d3.geo.path, coverage, and flaky tooltips",
        "dates": "2026-06-15 – 2026-06-21",
        "sprint": "Week 4",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "d3.geo.path and flaky tooltips",
        "progress_when": "Week 4 · June 15–21",
        "progress_title": "Chose d3.geo.path and slowed flaky tooltip checks",
        "progress_status": "RENDERER DECISION",
        "progress_blurb": "I tried a planar SVG fallback to raise Codecov, then followed Toby’s guidance to ignore coverage and use d3.geo.path. A short Sys.sleep in the helper reduced tooltip timing flakes.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>Two separate problems showed up on PR #328: Codecov still disliked the new JS, and some tooltip tests passed only some of the time. On 17 June I computed a planar SVG path string as a fallback, then preferred <code>d3.geo.path</code> when it existed. The idea was to execute both branches so coverage would rise without changing the picture. Toby asked why coverage would change, what a planar SVG path was, and why <code>d3.geo.path</code> would ever be missing. The honest answer was that I did not know how to pass Codecov and was guessing. He told me to ignore Codecov and use <code>d3.geo.path</code>.</p>
      <p>I added <code>Sys.sleep(0.3)</code> in <code>helper-function.R</code> because the browser sometimes painted <code>tooltipID</code> after the assertion ran. Then I dropped the dual-path coverage hack after review and started rewriting the renderer to <code>d3.geo.path</code> only. Coverage is not a reason to keep dead branches. If d3 is always present in the animint page, the fallback is noise. Flaky interactive tests are often timing, not geometry.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted to finish the <code>d3.geo.path</code> implementation, then start issue #258: move <code>getCommonChunk()</code> to C++.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
        <li><a href="https://github.com/animint/animint2/issues/258">Issue #258: getCommonChunk C++</a></li>
      </ul>
""",
    },
    {
        "id": "week-5",
        "file": "week-5.html",
        "badge": "Week 5",
        "title": "Holes on d3.geo.path; first C++ experiments",
        "dates": "2026-06-22 – 2026-06-28",
        "sprint": "Week 5",
        "status": "Complete",
        "prs": "2",
        "issues": "2",
        "home_title": "d3.geo.path done; start C++",
        "progress_when": "Week 5 · June 22–28",
        "progress_title": "Closed the path question and opened C++ work",
        "progress_status": "JS DONE · #258 STARTED",
        "progress_blurb": "PR #328 now uses d3.geo.path only. I started reading issue #258, sketched smoke tests for getCommonChunk(), and Toby asked me to share those tests in a PR rather than keeping them local.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>By 22 June the hole renderer used <code>d3.geo.path</code>, passed the tests, and matched the local visualization. I then switched attention to <a href="https://github.com/animint/animint2/issues/258">issue #258</a>. Toby still wanted the JS on #328 to match PR #326, including dropping a manual <code>"M" + points.join("L") + "Z"</code> path. I had misunderstood that request earlier. After the correction, only <code>d3.geo.path()</code> remained.</p>
      <p>I removed the custom planar path builder, set up the #258 codebase, and wrote preliminary tests for common-chunk detection. When Toby asked about those “smoke tests,” I explained they were just basic checks before a PR, then promised to open one. Unshared tests do not count as progress on this project. The expected unit of work is a pull request, even when the C++ is still rough.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted to open PR #342 with a simplified C++ inner compare, tests, and an explanation that can move into a vignette.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
        <li><a href="https://github.com/animint/animint2/issues/258">Issue #258</a></li>
      </ul>
""",
    },
    {
        "id": "week-6",
        "file": "week-6.html",
        "badge": "Week 6",
        "title": "A reviewable C++ fast path for getCommonChunk()",
        "dates": "2026-06-29 – 2026-07-05",
        "sprint": "Week 6",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Simplified getCommonChunk C++",
        "progress_when": "Week 6 · June 29–July 5",
        "progress_title": "Opened PR #342 with a smaller C++ compare",
        "progress_status": "PR #342 OPEN · 38 TESTS",
        "progress_blurb": "Toby asked to shrink 300+ lines of C++. I opened PR #342 with ~154 lines, R grouping, C++ inner NA/matrix compare, 11 unit tests, and a vignette, then spent days stripping accidental CRAN artifacts.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>On 29 June I opened <a href="https://github.com/animint/animint2/pull/342">PR #342</a> for issue #258. The first C++ was too large. After Toby asked for something closer to 100 lines, I kept grouping in R and moved only the inner compare to <code>common_value_for_group_subset_cpp()</code> (~154 lines). <code>getCommonChunk()</code> splits compiled plot data so the browser only downloads values that change with a selector. After earlier correctness work, the remaining cost was the inner “is this column constant across chunks?” loop, including NA handling.</p>
      <p>I wired Rcpp exports, an <code>options(animint2.use.cpp)</code> R fallback, and 11 unit tests (38 expectations passing). I moved the markdown explanation into <code>vignettes/get-common-chunk-cpp.Rmd</code>. Then CRAN and coverage CI failed for packaging reasons: I had committed <code>src/get_common_chunk.o</code>, knitted HTML instead of the <code>.Rmd</code>, and <code>useDynLib</code> was being stripped by <code>devtools::document()</code> in the CRAN script. I added <code>R/rcpp-dynlib.R</code>, gitignored build artifacts, and stripped the vignette from the CRAN tarball in <code>build.sh</code>.</p>
      <p>CRAN CI is a packaging problem as much as a code problem. Object files, knitted vignettes, and NAMESPACE generation can fail a check even when tests pass locally on Windows with Rtools.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted review on both #328 and #342 before midterm.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
        <li><a href="https://github.com/animint/animint2/issues/258">Issue #258</a></li>
      </ul>
""",
    },
    {
        "id": "week-7",
        "file": "week-7.html",
        "badge": "Week 7",
        "title": "Midterm: two PRs in review, then illness",
        "dates": "2026-07-06 – 2026-07-12",
        "sprint": "Week 7",
        "status": "Complete",
        "prs": "2",
        "issues": "2",
        "home_title": "Midterm review checkpoint",
        "progress_when": "Week 7 · July 6–12",
        "progress_title": "Asked for merges, then had a slow week",
        "progress_status": "MIDTERM · LIMITED CODING",
        "progress_blurb": "I pinged Toby that #328 looked merge-ready and that #342 stayed near 154 lines of C++ with a vignette. I was sick 7–12 July and could not work much.",
        "body": """
      <h2 id="the-week">The week</h2>
      <p>Midterm week was a status checkpoint more than a feature week. On 6 July I asked for a review of PR #328, which I believed was ready to merge, and of PR #342’s simplified C++ plus vignette. The midterm plan on issue #322 was exactly these two branches: get polygon holes merge-ready, and keep the C++ PR reviewable while CI goes green.</p>
      <p>I summarized both PRs for mentors, then did not push substantial new code from 7–12 July while sick. Public updates still matter in a quiet week. The issue log is how mentors see that a PR is waiting rather than abandoned.</p>

      <h2 id="next">Looking ahead</h2>
      <p>Next I wanted to return to Yufan’s review comments on #342 as soon as they land.</p>

      <h2 id="links">Links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/issues/322">Issue #322</a></li>
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
      </ul>
""",
    },
    {
        "id": "week-8",
        "file": "week-8.html",
        "badge": "Week 8",
        "title": "Implementing Yufan’s C++ review",
        "dates": "2026-07-13 – 2026-07-19",
        "sprint": "Week 8",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Yufan’s review on PR #342",
        "progress_when": "Week 8 · July 13–19",
        "progress_title": "Coded the first round of C++ review comments",
        "progress_status": "REVIEW IMPLEMENTATION",
        "progress_blurb": "Yufan left review on PR #342. I read the comments, translated them into code, and kept the inner-compare design intact.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>After the sick week I used 16–20 July to work through Yufan’s review on <a href="https://github.com/animint/animint2/pull/342">PR #342</a>.</p>

      <h2 id="context">Context</h2>
      <p>The C++ still had to stay small, match R’s NA/matrix/scalar compare, and remain optional via an R fallback. Review comments were about making that contract obvious, not rewriting grouping yet.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>Read the inline discussion and applied the requested changes.</li>
        <li>Re-ran the compiler unit tests after each edit.</li>
      </ul>

      <h2 id="next">Next week targets</h2>
      <p>Finish the remaining #342 comments and get the test file fully green again.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
      </ul>
""",
    },
    {
        "id": "week-9",
        "file": "week-9.html",
        "badge": "Week 9",
        "title": "C++ tests green, no obvious timing issues",
        "dates": "2026-07-20 – 2026-07-26",
        "sprint": "Week 9",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "PR #342 tests passing",
        "progress_when": "Week 9 · July 20–26",
        "progress_title": "Finished review fixes; tests and atime looked clean",
        "progress_status": "TESTS PASSING",
        "progress_blurb": "I corrected the remaining #342 review items. By 30 July the tests passed and the atime job did not show obvious timing issues versus master.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>21–25 July I finished the next review thread on PR #342. By the end of the month the test file was green and the atime comment on the PR did not show a timing regression.</p>

      <h2 id="context">Context</h2>
      <p>Toby later asked for a working atime CI job and a test before merge, so that reviewers can see a speedup rather than only a C++ file. This week was the setup for that evidence.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>Applied the remaining C++/R review corrections.</li>
        <li>Confirmed unit tests still passed after the edits.</li>
      </ul>

      <h2 id="next">Next week targets</h2>
      <p>Fix merge conflicts and test failures on PR #328, and post a full status comment on #342.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
      </ul>
""",
    },
    {
        "id": "week-10",
        "file": "week-10.html",
        "badge": "Week 10",
        "title": "Conflicts on holes; status write-up on C++",
        "dates": "2026-07-27 – 2026-08-02",
        "sprint": "Week 10",
        "status": "Complete",
        "prs": "2",
        "issues": "2",
        "home_title": "Merge conflicts and PR status",
        "progress_when": "Week 10 · July 27–August 2",
        "progress_title": "Unblocked #328 conflicts and summarized #342",
        "progress_status": "2 PRS ADVANCED",
        "progress_blurb": "Toby asked me to fix conflicts and test failures on PR #328. I did that on 31 July, ignored atime/codecov there, and posted a full ready-for-review status on PR #342 on 2 August.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>Two long-running PRs both moved. Polygon holes needed a rebase; the C++ PR needed a clear status for mentors who had not looked in a few weeks.</p>

      <h2 id="context">Context</h2>
      <p>On 29 July Toby asked what the status of #342 was, and separately asked me to fix conflicts on #328. atime on #342 already showed HEAD faster for the getCommonChunk workload in the CML plot.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>31 July: resolved merge conflicts and test failures on PR #328. Left atime and Codecov alone on that branch.</li>
        <li>2 August: wrote a status comment on #342: simplified C++, unit tests passing, Yufan’s comments addressed, atime #258 test up.</li>
      </ul>

      <h2 id="learnings">Learnings</h2>
      <p>A PR that sits through midterm needs a periodic “here is what is true today” comment. Mentors should not have to reconstruct status from commits.</p>

      <h2 id="next">Next week targets</h2>
      <p>Wait on review, and ping all three mentors if #342 is still untouched.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328</a></li>
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
      </ul>
""",
    },
    {
        "id": "week-11",
        "file": "week-11.html",
        "badge": "Week 11",
        "title": "Waiting on review, then asking again",
        "dates": "2026-08-03 – 2026-08-09",
        "sprint": "Week 11",
        "status": "Complete",
        "prs": "1",
        "issues": "1",
        "home_title": "Waiting on C++ review",
        "progress_when": "Week 11 · August 3–9",
        "progress_title": "Held #342 and pinged mentors",
        "progress_status": "REVIEW WAIT",
        "progress_blurb": "There was no major new commit. After the 2 August status I waited, then on 7 August asked Toby, Yufan, and Suhaani to review PR #342.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>Week 11 was a review wait. I did not want to pile extra C++ onto #342 while mentors were still looking at the simplified design.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>Watched CI on the open branches.</li>
        <li>On 7 August requested review from <code>@tdhock</code>, <code>@Faye-yufan</code>, and <code>@suhaani-agarwal</code>.</li>
      </ul>

      <h2 id="next">Next week targets</h2>
      <p>Respond immediately to whatever the atime and design review says.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
      </ul>
""",
    },
    {
        "id": "week-12",
        "file": "week-12.html",
        "badge": "Week 12",
        "title": "Move the grouping loop to C++; fix Codecov uploads",
        "dates": "2026-08-10 – 2026-08-16",
        "sprint": "Week 12",
        "status": "Complete",
        "prs": "2",
        "issues": "2",
        "home_title": "C++ group scan and Codecov CI",
        "progress_when": "Week 12 · August 10–16",
        "progress_title": "Hit the real getCommonChunk bottleneck; opened #344",
        "progress_status": "ATIME SPEEDUP · PR #344",
        "progress_blurb": "Suhaani showed that Fast/Slow overlapped because grouping was still in R. I added detect_common_value_dt_cpp, fixed the atime workload, and opened PR #344 so R and JS coverage upload together after both jobs succeed.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>Suhaani’s review on 10 August was the important one: tests passed, but atime Fast/Slow overlapped (p≈0.84) because the <code>by=</code> grouping loop was still in R. Issue #258 had called out that loop as the slow part.</p>
      <p>I moved the column/group scan to C++ as <code>detect_common_value_dt_cpp</code> and fixed the atime workload so it actually builds a common chunk. HEAD became much faster (about 65× on the predicted N, p=0). Locally, 20k rows / 5k groups went from ~23s in R to ~0.5s in C++.</p>

      <h2 id="context">Context</h2>
      <p>The earlier ~154-line design was easier to review but did not hit the bottleneck. I also started <a href="https://github.com/animint/animint2/issues/254">issue #254</a>: Codecov <code>project</code> dropped on doc-only commits because R and JS uploaded separately. A failed JS job became the baseline.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>Implemented <code>detect_common_value_dt_cpp</code> and merged master (DESCRIPTION version conflict).</li>
        <li>Opened <a href="https://github.com/animint/animint2/pull/344">PR #344</a>: save both coverage reports as artifacts and upload them together only after both jobs succeed; skip PDF <code>knit_print</code> tests when <code>pdflatex</code> is missing so coverage jobs need no texlive.</li>
      </ul>

      <h2 id="learnings">Learnings</h2>
      <p>A benchmark that returns early with no common chunk will never show a speedup. The atime SHA labeled Fast also has to be the implementation you claim is fast.</p>

      <h2 id="next">Next week targets</h2>
      <p>Explain the Fast vs Slow vs HEAD atime curves, and keep #328 moving toward merge.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
        <li><a href="https://github.com/animint/animint2/pull/344">PR #344</a></li>
        <li><a href="https://github.com/animint/animint2/issues/254">Issue #254</a></li>
      </ul>
""",
    },
    {
        "id": "final-submission",
        "file": "final-submission.html",
        "badge": "Final submission",
        "title": "Polygon holes merged; C++ and Codecov still open",
        "dates": "2026-08-17 – 2026-08-24",
        "sprint": "Final",
        "status": "Complete",
        "prs": "3",
        "issues": "3",
        "home_title": "First merge and remaining PRs",
        "progress_when": "Final Submission · August 17–24",
        "progress_title": "PR #328 merged; #342 and #344 still in review",
        "progress_status": "1 MERGED · 2 OPEN",
        "progress_blurb": "Toby merged PR #328 on 14 August. I explained why atime Fast still tracked Slow, retargeted the Fast SHA, and started the polygon-holes post for animint-blog after Toby asked for a user-facing write-up.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>The first GSoC merge landed: <a href="https://github.com/animint/animint2/pull/328">PR #328</a> on 14 August, with polygon holes via <code>subgroup</code> and the <code>tooltipID()</code> test helper. End-term work stayed on #342 and #344.</p>

      <h2 id="context">Context</h2>
      <p>Toby asked why the atime Fast curve was almost as large as Slow. Slow is the old R <code>by=</code> path. Fast is the earlier C++ that only moved the inner compare. HEAD is <code>detect_common_value_dt_cpp</code>. Suhaani asked me to retarget <code>Fast=</code> in <code>.ci/atime/tests.R</code> so the labeled Fast curve matches HEAD, and said the rest looked good.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>Merged master into the C++ branch and posted the Fast/Slow/HEAD explanation.</li>
        <li>Toby asked Gaurav to review #344.</li>
        <li>On 19 August Toby asked for a blog post about the new hole feature on <a href="https://animint-blog.netlify.app/">animint-blog</a>.</li>
      </ul>

      <h2 id="learnings">Learnings</h2>
      <p>atime labels are part of the review. If Fast is an old SHA, reviewers will think the optimization failed even when HEAD is fast.</p>

      <div class="diagram" aria-label="atime curve meanings">
        <div class="diagram-col is-risk">
          <p><strong>Slow / Fast</strong></p>
          <p>Old R grouping, or C++ that only compared values after R still grouped with <code>by=</code>. Curves overlap. No real win.</p>
        </div>
        <div class="diagram-arrow">→</div>
        <div class="diagram-col is-safe">
          <p><strong>HEAD</strong></p>
          <p><code>detect_common_value_dt_cpp</code> scans columns and groups in C++. This is the curve that should be labeled Fast.</p>
        </div>
      </div>

      <h2 id="next">Next week targets</h2>
      <p>Open the animint-blog PR, address Gaurav’s #344 comments, and keep #342 merge-ready.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint2/pull/328">PR #328: merged 14 Aug 2026</a></li>
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
        <li><a href="https://github.com/animint/animint2/pull/344">PR #344</a></li>
      </ul>
""",
    },
    {
        "id": "end-term",
        "file": "end-term.html",
        "badge": "End term",
        "title": "Feature blog, Codecov review, and NEWS.md",
        "dates": "2026-08-24 – 2026-09-07",
        "sprint": "End term",
        "status": "In progress",
        "prs": "3",
        "issues": "2",
        "home_title": "Blog post and end-term polish",
        "progress_when": "End term · August 24–September 7",
        "progress_title": "Documented holes and finished #344 review threads",
        "progress_status": "BLOG OPEN · #344 READY",
        "progress_blurb": "I opened animint-blog#2, addressed Gaurav’s Codecov review, fixed blog knit errors, resolved #344 merge conflicts, and corrected a CRAN NEWS.md NOTE. #342 and #344 remain the end-term merge targets.",
        "body": """
      <h2 id="outcome">Outcome</h2>
      <p>End term split across a user-facing blog and the remaining infrastructure PRs. <a href="https://github.com/animint/animint-blog/pull/2">animint-blog#2</a> explains how to draw polygon holes and why they matter for hover and click. <a href="https://github.com/animint/animint2/pull/344">PR #344</a> absorbed Gaurav’s review and a CRAN NEWS note.</p>

      <h2 id="context">Context</h2>
      <p>Toby wanted the blog focused on using holes, with some historical context (the 2018 fork versus ggplot2 3.2.0 <code>subgroup</code>), not a changelog of tests. Gaurav’s #344 review asked for covr Rlang JSON handling, PDF tests on the CRAN job, restoring the JS coverage download, and loading animint2 before the CRAN PDF renderer test. He said the PR looked good on 27 August.</p>

      <h2 id="what-i-did">What I did</h2>
      <ul>
        <li>24–31 August: opened the blog PR; applied Gaurav’s CI comments on #344.</li>
        <li>1–7 September: rewrote the post around usage and interaction; fixed a <code>data.table</code> parse error and a discrete-scale error by making <code>num</code> a factor and setting <code>scale_fill_manual(values=...)</code>.</li>
        <li>Resolved #344 merge conflicts, then fixed <code>NEWS.md</code> so CRAN could parse <code>Changes in development (PR#339)</code>.</li>
        <li>Asked Toby to review #344 again.</li>
      </ul>

      <h2 id="learnings">Learnings</h2>
      <p>A package blog is a vignette in public: the examples have to knit in CI. CRAN NEWS section titles are a real check, not decoration.</p>

      <h2 id="next">Next week targets</h2>
      <p>Merge #344 after Toby’s pass. On #342, keep atime showing a HEAD speedup, finish the vignette hosting link, and get the grouping-scan C++ through final review.</p>

      <h2 id="evidence">Evidence and links</h2>
      <ul class="evidence-list">
        <li><a href="https://github.com/animint/animint-blog/pull/2">animint-blog#2: polygon holes post</a></li>
        <li><a href="https://github.com/animint/animint2/pull/344">PR #344</a></li>
        <li><a href="https://github.com/animint/animint2/pull/342">PR #342</a></li>
        <li><a href="https://github.com/animint/animint2/issues/322">Issue #322: source updates</a></li>
      </ul>
""",
    },
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


home_cards = "\n".join(
    f'        <a href="./journal/{w["file"]}"><strong>{w["badge"]}</strong><br>{w["home_title"]}</a>'
    for w in WEEKS
    if w["id"].startswith("week-")
)

home = page(
    "GSoC 2026 Animint2 Development Journal – Nishita / GSoC 2026",
    "A public engineering journal documenting Nishita Shah's Google Summer of Code 2026 journey with Animint2.",
    "home",
    ".",
    extra_class="home-page",
    body=f"""
    <div class="journal-hero">
      <p class="eyebrow">Google Summer of Code 2026</p>
      <h1>Welcome to my GSoC 2026 Journey</h1>
      <p>Follow my journey through Google Summer of Code 2026, where I, <strong>Nishita Shah</strong> (GitHub: <strong>Nishita-shah1</strong>), share weekly updates, review cycles, and implementation notes from the Animint2 project. This journal is compiled from my public log on <a href="https://github.com/animint/animint2/issues/322">animint2#322</a>.</p>
      <div class="hero-actions">
        <a class="journal-button journal-button-primary" href="./journal/index.html">Open journal</a>
        <a class="journal-button journal-button-secondary" href="./future.html">For future developers</a>
      </div>
    </div>

    <h2>About the project</h2>
    <div class="editorial-panel">
      <p>My GSoC project improves Animint2, an R package for animated and interactive data visualizations. I worked on polygon holes in the renderer, a C++ fast path for <code>getCommonChunk()</code>, Codecov CI reliability, tests, and a user-facing blog post. The goal is to make Animint2 faster to compile, correct for hole geometry, and easier to review in CI.</p>
    </div>

    <h2>Development journey</h2>
    <div class="week-card-grid">
{home_cards}
    </div>

    <p>Community bonding, the August final window, and end-term review are in the journal as well: <a href="./journal/community-bonding.html">bonding</a> · <a href="./journal/final-submission.html">final submission</a> · <a href="./journal/end-term.html">end term</a>.</p>

    <h2>Contributions</h2>
    <table class="contrib-table">
      <thead>
        <tr><th>PR</th><th>Issue</th><th>Status</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><a href="https://github.com/animint/animint2/pull/328">#328</a></td>
          <td><a href="https://github.com/animint/animint2/issues/252">#252</a>: polygon holes via <code>subgroup</code> + <code>tooltipID()</code></td>
          <td><span class="status-pill">Merged 14 Aug 2026</span></td>
        </tr>
        <tr>
          <td><a href="https://github.com/animint/animint2/pull/342">#342</a></td>
          <td><a href="https://github.com/animint/animint2/issues/258">#258</a>: <code>getCommonChunk()</code> C++ speedup</td>
          <td><span class="status-pill">Open</span></td>
        </tr>
        <tr>
          <td><a href="https://github.com/animint/animint2/pull/344">#344</a></td>
          <td><a href="https://github.com/animint/animint2/issues/254">#254</a>: combined R+JS Codecov upload</td>
          <td><span class="status-pill">Open</span></td>
        </tr>
        <tr>
          <td><a href="https://github.com/animint/animint-blog/pull/2">animint-blog#2</a></td>
          <td>How to draw polygon holes, and why hover/click need them</td>
          <td><span class="status-pill">Open</span></td>
        </tr>
      </tbody>
    </table>
""",
)

progress_entries = []
for w in WEEKS:
    node = {
        "community-bonding": "CB",
        "final-submission": "FS",
        "end-term": "ET",
    }.get(w["id"], w["badge"].replace("Week ", "W").replace(" ", ""))
    if node.startswith("Week"):
        node = f"W{int(w['id'].split('-')[1]):02d}"
    if w["id"].startswith("week-"):
        node = f"W{int(w['id'].split('-')[1]):02d}"
    progress_entries.append(f"""
    <article class="progress-timeline-entry">
      <div class="progress-timeline-copy">
        <p class="when">{w["progress_when"]}</p>
        <h2>{w["progress_title"]}</h2>
        <p class="progress-timeline-status">{w["progress_status"]}</p>
        <p>{w["progress_blurb"]}</p>
        <p><a class="progress-journal-link" href="./journal/{w["file"]}">Read journal</a></p>
      </div>
      <div class="progress-timeline-node" aria-hidden="true">{node}</div>
    </article>
""")

progress = page(
    "Progress Report – Nishita / GSoC 2026",
    "A scan-friendly timeline of Nishita Shah's GSoC 2026 Animint2 work.",
    "progress",
    ".",
    extra_class="progress-page",
    body=f"""
    <div class="progress-report-heading"><h1>Progress Report</h1></div>
    <div class="progress-intro-panel">
      <h2>Timeline of contributions</h2>
      <p>Fifteen entries from issue #322: community bonding, twelve coding weeks, the August final-submission window, and end-term review through 7 September 2026.</p>
    </div>
    <div class="progress-timeline" aria-label="GSoC 2026 project timeline">
      {''.join(progress_entries)}
    </div>
""",
)

about = page(
    "About Nishita Shah – Nishita / GSoC 2026",
    "Nishita Shah's GSoC 2026 contributor profile and Animint2 project overview.",
    "about",
    ".",
    extra_class="about-page",
    body="""
    <section class="about-profile">
      <div class="about-profile-media">
        <img class="about-profile-portrait" src="https://github.com/Nishita-shah1.png" alt="Portrait of Nishita Shah">
      </div>
      <div class="about-profile-content">
        <p class="eyebrow">About</p>
        <h1 class="about-profile-name">Nishita Shah</h1>
        <a class="about-profile-handle" href="https://github.com/Nishita-shah1">↗ Nishita-shah1</a>
        <div class="about-profile-intro">
          <p>I am a Google Summer of Code 2026 contributor working on Animint2 with the R Project for Statistical Computing. My work focuses on renderer correctness for polygon holes, C++ compile-time performance, tests, and CI reliability.</p>
          <p>This journal documents implementation progress, review decisions, and verified contributions throughout the project.</p>
        </div>
        <div class="about-project-block">
          <p class="eyebrow">GSoC 2026 project</p>
          <h2>Advancing Animint2: holes, compile speed, and coverage CI</h2>
          <div class="about-project-meta">
            <div class="about-project-detail">
              <h3>Organization</h3>
              <p>R Project for Statistical Computing</p>
            </div>
            <div class="about-project-detail">
              <h3>Mentors</h3>
              <p>Toby Dylan Hocking · Yufan Fei · Suhaani Agarwal</p>
            </div>
          </div>
          <div class="about-tag-section">
            <h3>Technologies</h3>
            <div class="tag-list">
              <code>R</code><code>JavaScript</code><code>C++</code><code>D3.js</code><code>Rcpp</code><code>GitHub Actions</code>
            </div>
          </div>
          <div class="about-tag-section">
            <h3>Focus areas</h3>
            <div class="tag-list">
              <code>Testing</code><code>Data visualization</code><code>Performance</code><code>CI</code>
            </div>
          </div>
        </div>
      </div>
    </section>
    <h2>Contribution links</h2>
    <div class="about-links">
      <a class="about-link" href="https://github.com/animint/animint2">Animint2 repository ↗</a>
      <a class="about-link" href="https://github.com/animint/animint2/issues/322">GSoC updates issue ↗</a>
    </div>
""",
)

contact = page(
    "Contact – Nishita / GSoC 2026",
    "Contact Nishita Shah and explore her Animint2 and GSoC 2026 project links.",
    "contact",
    ".",
    extra_class="contact-page",
    body="""
    <div class="contact-hero">
      <h1>Contact me</h1>
      <p>Open to conversations around GSoC, Animint2, open source, and software engineering.</p>
    </div>
    <div class="contact-panel">
      <p class="contact-panel-intro">Reach me through the channels below. Daily project notes live on GitHub issue #322.</p>
      <div class="contact-method-grid">
        <a class="contact-method-card" href="https://github.com/Nishita-shah1" target="_blank" rel="noopener noreferrer">
          <span class="contact-method-name">GitHub</span>
          <span class="contact-method-detail">@Nishita-shah1</span>
        </a>
        <a class="contact-method-card" href="https://github.com/animint/animint2/issues/322" target="_blank" rel="noopener noreferrer">
          <span class="contact-method-name">GSoC log</span>
          <span class="contact-method-detail">animint2#322</span>
        </a>
      </div>
      <div class="contact-quick-links">
        <h2>Quick links</h2>
        <div class="contact-quick-link-grid">
          <a class="contact-quick-link" href="https://github.com/animint/animint2">Animint2 repository</a>
          <a class="contact-quick-link" href="https://github.com/rstats-gsoc/gsoc2026/wiki/Animated-interactive-ggplots">GSoC 2026 project idea</a>
          <a class="contact-quick-link" href="https://Nishita-shah1.github.io/animint-viz/">Gradient descent viz</a>
        </div>
      </div>
    </div>
""",
)


def main() -> None:
    write(ROOT / "index.html", home)
    write(ROOT / "progress.html", progress)
    write(ROOT / "about.html", about)
    write(ROOT / "contact.html", contact)

    journal_dir = ROOT / "journal"
    first = next(w for w in WEEKS if w["id"] == "week-1")
    write(
        journal_dir / "index.html",
        page(
            f'{first["title"]} – Nishita / GSoC 2026',
            first["title"],
            "journal",
            "..",
            extra_class="week-page",
            week_nav=True,
            toc=True,
            body=week_header(first["badge"], first["title"], first["dates"])
            + first["body"],
        ),
    )
    for w in WEEKS:
        write(
            journal_dir / w["file"],
            page(
                f'{w["title"]} – Nishita / GSoC 2026',
                w["title"],
                f'journal-{w["id"]}',
                "..",
                extra_class="week-page",
                week_nav=True,
                toc=True,
                body=week_header(w["badge"], w["title"], w["dates"])
                + w["body"],
            ),
        )
    print("Wrote site pages.")


if __name__ == "__main__":
    main()
