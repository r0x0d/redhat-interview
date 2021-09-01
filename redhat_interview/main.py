import sys

try:
    import dnf
except:
    # Just a little check to produce a better output for the user.
    required_dependency = (
        "python3-dnf" if not sys.version_info <= (3,) else "python2-dnf"
    )
    raise SystemExit(
        "Failed to load dnf package as a module.\nMake sure you have installed the {} in your system.".format(
            required_dependency
        )
    )

# The name of the package to search using the dnf api.
# Since this is an simple application to only list the versions of the
# kernel installed on the system, we let it be hardcoded here to simplify usage.
# If any other package would be used in the search, this should be renamed for the correct package name.
DNF_SEARCH_PACKAGE_NAME = "kernel"


def get_installed_dnf_packages():
    """Method to retrieve the installed packages in the current running system."""

    # Initialize the Base API for the dnf module and then
    # load up the sack of metadata information used in dnf
    # to be able to return a query object containing the packages of the system
    base = dnf.Base()
    base.fill_sack()
    query = base.sack.query()

    # Return the installed packages
    return query.installed()


def main():
    """Main entrypoint for the simple application to output the currently installed kernel versions"""

    # Collect the installed packages using the dnf api
    print(
        "Getting installed versions for the package: '{}'".format(
            DNF_SEARCH_PACKAGE_NAME
        )
    )
    packages = get_installed_dnf_packages()

    # Filter for the specific package definied in DNF_SEARCH_PACKAGE_NAME constant
    filtered_packages = packages.filter(name=DNF_SEARCH_PACKAGE_NAME)

    # Loop through the results for the filtered package and output the version collected from the hawkey
    print("Found a total of '{}' versions installed\n".format(len(filtered_packages)))
    for package in filtered_packages:
        print(package.version)


if __name__ == "__main__":
    main()
