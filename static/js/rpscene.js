function addCreateToSelect(select) {
    let createModal = $("#selectwithcreate-modal");
    // Create modal if not existent
    if (!createModal.length) {
        createModal = $('<div class="modal">\n' +
            '    <div class="modal-background"></div>\n' +
            '    <div class="modal-content"></div>\n' +
            '    <button class="modal-close is-large" aria-label="close"></button>\n' +
            '</div>');
        $(document.body).append(createModal);
    }

    let createUrl = select.attr("create-url");
    let updateUrl = select.attr("update-url");

    let formField = select.closest(".field");
    let addonField = $('<div class="field has-addons"/>');

    let createButton = $('<a class="button is-success" href=""><span class="icon is-small"><i class="fas fa-plus"></i></span></a>');
    let createHelp = $('<div class="help"/>');

    addonField.append(formField.children(".control"));
    addonField.append(createButton);
    createButton.wrap($('<div class="control"/>'));

    formField.append(addonField);
    formField.append(createHelp);

    createButton.click(function () {
        createModal.children(".modal-content").load(createUrl, function (response, status, xhr) {
            createModal.toggleClass("is-active").hide().fadeIn("fast");

            createModal.children(".modal-content").find("form").submit(function (e) {
                e.preventDefault();
                $.ajax({
                    type: $(this).attr('method'),
                    url: createUrl,
                    data: $(this).serialize(),
                    success: function (xhr, ajaxOptions, thrownError) {
                        select.load(updateUrl, function () {
                            select.find('option[value="' + xhr["id"] + '"]').prop("selected", true);
                        });

                        createModal.fadeOut("fast", function () {
                            $(this).toggleClass("is-active");
                        });

                        createHelp.addClass("is-success").text("Added element!").delay(5000).fadeOut("fast", function () {
                            $(this).removeClass("is-success")
                        });
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        createHelp.addClass("is-danger").text("Could not add element!").delay(5000).fadeOut("fast", function () {
                            $(this).removeClass("is-danger")
                        });
                    }
                });
            });
        });

        return false;
    });

    createModal.children(".modal-close, .modal-background").click(function () {
        createModal.fadeOut("fast", function () {
            $(this).toggleClass("is-active");
        });
    });
}

$(document).ready(function () {
    $("select[select-with-create]").each(function () {
        addCreateToSelect($(this));
    });
});