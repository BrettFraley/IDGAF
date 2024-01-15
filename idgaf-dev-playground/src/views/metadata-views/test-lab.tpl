% rebase('./views/base.tpl')
<div class="container">
    <div class="px-4 pt-5 my-5 border-bottom">
        <h1 class="display-4 fw-bold text-body-emphasis">Test Lab</h1>
    </div>

    <a href="/test-lab/git-history" class="secondary">Git History</a>
    <div id="git-history">
        <div class="test-lab-shell-output">
            <p>Git History</p>
            <hr>
            {% if gitHistory %}
                {{ gitHistory }}
            {% end %}
        </div>
    </div>
</div>
