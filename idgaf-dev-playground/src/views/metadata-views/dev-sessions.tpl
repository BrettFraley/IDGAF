% rebase('./views/base.tpl')
<div class="container">
    <div class="px-4 pt-5 my-5 border-bottom">
        <h1 class="display-4 fw-bold text-body-emphasis">Dev Sessions</h1>

        % for row in sessions:
            <p>{{ row }}</p>
        % end

        <!-- New Dev Session-->
        <div class="row">
            <p>New Dev Session</p>
            <form action="/new-dev-session" method="POST" enctype="multipart/form-data">
                <div class="row g-3 m-3">

                    <div class="col-md-4">
                        <label for="developer" class="form-label m-1">Developer</label>
                        <input type="text" class="form-control border border-dark" placeholder="..." aria-label="Developer Name" name="developer">
                    </div>
                    <div class="col-md-4">
                        <label for="Session Name" class="form-label m-1">Session Name</label>
                        <input type="text" class="form-control border border-dark" placeholder="..." aria-label="Session Name" name="sessionName">
                    </div>

                    <div class="col-md-4">
                        <label for="Session Type" class="form-label m-1">Session Type</label>
                        <select class="form-select border border-dark" aria-label="Session Type" placeholder="Choose" name="sessionType">
                            
                            <option value="Feature">Feature</option>
                            <option value="Story">User Story</option>
                            <option value="Update">Content Update</option>
                            <option value="Issue/Bug">Issue/Bug</option>
                            <option value="Misc">Miscellaneous</option>
                        </select>
                    </div>
                </div>

                <div class="row mt-3">
                    <label for="description" class="form-label m-1">Description</label>
                    <textarea class="form-control border border-dark m-2" rows="3" name="description"></textarea>
                </div>

                <button type="submit" class="btn btn-secondary mt-3">Submit</button>
        
            </form>

        </div>

        <!-- New Dev Session Table-->
        <div class="row">
            <p>Create New Dev Session Table</p>
            <form action="/new-dev-session-table" method="POST" enctype="multipart/form-data">
                <div class="row">
P
                    <div class="col-3">
                        <label for="tableName">Table Name</label>
                        <input type="text" class="form-control border border-dark" placeholder="Table Name" aria-label="Table Name" name="tableName">
                    </div>
                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
        
            </form>

        </div>


    </div>
</div>
