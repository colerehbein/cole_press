# Makefile for cole_press
# Quarto-based personal website at cole.press

.PHONY: help preview build render setup clean install-r-deps install-tinytex check

# Default target
help:
	@echo "cole_press - Quarto website build commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Development:"
	@echo "  preview       Start local dev server with hot reload (port 4200)"
	@echo "  build         Render site to _site/"
	@echo "  render        Alias for build"
	@echo ""
	@echo "Setup:"
	@echo "  setup         Install R packages and TinyTeX"
	@echo "  install-r-deps  Install R packages from DESCRIPTION"
	@echo "  install-tinytex Install TinyTeX for PDF generation"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean         Remove generated files (_site, _freeze, caches)"
	@echo "  check         Verify Quarto and R installation"
	@echo ""

# Development
preview:
	quarto preview --port 4200

build:
	quarto render

render: build

# Setup
setup: install-r-deps install-tinytex
	@echo "✅ Setup complete!"

install-r-deps:
	@echo "Installing R packages from DESCRIPTION..."
	R -e "dir.create(Sys.getenv('R_LIBS_USER'), recursive=TRUE, showWarnings=FALSE); install.packages(c('knitr', 'rmarkdown'), repos='https://cloud.r-project.org', lib=Sys.getenv('R_LIBS_USER'))"

install-tinytex:
	@echo "Installing TinyTeX for PDF generation..."
	quarto install tinytex --no-prompt || true

# Maintenance
clean:
	@echo "Removing generated files..."
	rm -rf _site/
	rm -rf _freeze/
	rm -rf *_cache/
	rm -rf .quarto/
	@echo "✅ Clean complete!"

# Verification
check:
	@echo "Checking installation..."
	@echo ""
	@echo "Quarto:"
	@quarto --version || echo "❌ Quarto not found"
	@echo ""
	@echo "R:"
	@R --version | head -1 || echo "❌ R not found"
	@echo ""
	@echo "R packages:"
	@R -e "cat('knitr:', as.character(packageVersion('knitr')), '\n')" 2>/dev/null || echo "❌ knitr not installed"
	@R -e "cat('rmarkdown:', as.character(packageVersion('rmarkdown')), '\n')" 2>/dev/null || echo "❌ rmarkdown not installed"
	@echo ""
	@echo "TinyTeX:"
	@quarto list tools | grep -i tinytex || echo "TinyTeX status unknown"
