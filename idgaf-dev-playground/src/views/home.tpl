% rebase('./views/base.tpl')

<div class="container">
    <div class="px-4 pt-5 my-5 text-center border-bottom">

        <h1 class="display-4 fw-bold text-body-emphasis landing-headline">
            IDGAF Dev Playground
        </h1>
        
        <div class="col-lg-8 mx-auto" id="test-bg">
            <p class="lead mb-4 fs-5">Notes:</p>
            <p class="lead mb-4 fs-5">test</p>
            <p class="lead mb-4 fs-5">test</p>
            <p class="lead mb-4 fs-4">I D G A F</p>
        
            <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
                <a href="/"><button type="button" class="btn btn-outline-secondary  btn-lg px-4 me-sm-3">Launch Main</button></a>
                <button type="button" class="btn btn-outline-secondary active btn-lg px-4">Build Commands</button>
            </div>
        </div>

    </div>
</div>

<div class="container-fluid ">
    <div class="row justify-content-md-center">

        <div class="col-4">
            <p>Notes / TODO</p>
            <ul>
                <li>Save all this as a scaffold as a template for other versions, or feature development</li>
                <li>Get SQLite DB Management UI features made first</li>
                <li>Get Server/Build/Depoyment config setup and 'configurable'</li>
                <li>Get the idea of labs/experiements set up where I can launch a 'scaffold' or 'copy' or 'test' from this UI</li>
            </ul>

            <ul>
                <li>Need console ouuput UI for monitoring network, sessions, cookies, headers..etc</li>
                <li>Need server error debug UI and or log feed and metrics UI dash</li>
                <li>Performance log UI</li>
                <li>Design / CSS engine and lib management UI</li>
            </ul>
        </div>

        <div class="col-4">

            <p>Need to have a test environment available from this UI
                to run on code generation functions. So, iut's like click
                button, code generates, and then is returned and rendered
                all in the UI. This way generated UI code can be verified
                and adjusted on the fly.
            </p>

            <p>
                Many of the tools and features that get built into this dev playground
                will end up being features of the framework itself and the end users experience.
            </p>
        </div>

        </div>
    </div>
</div>
