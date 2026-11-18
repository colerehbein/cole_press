# Makefile for cole_press
# Quarto-based personal website at cole.press

.PHONY: help preview build render setup clean install-tinytex check status cv-sync

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
	@echo "  setup         Install TinyTeX (for the CV PDFs)"
	@echo "  install-tinytex Install TinyTeX for PDF generation"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean         Remove generated files (_site, _freeze, caches)"
	@echo "  check         Verify Quarto and R installation"
	@echo ""

# Development
preview:
	quarto preview --port 4200

build: status
	quarto render

# Refresh the NOW bar (_status.qmd) before rendering. Fails soft: no network
# leaves the committed snapshot in place (same contract as CI).
status:
	node scripts/status-bar.mjs || true

render: build

# Setup
setup: install-tinytex
	@echo "✅ Setup complete!"

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

# CV: sync canonical full CV from colerehbein/cv repo (SOURCE defaults to ../cv)
cv-sync:
	@bash scripts/cv-sync.sh $(filter-out $@,$(MAKECMDGOALS))

# Verification
check:
	@echo "Checking installation..."
	@echo ""
	@echo "Quarto:"
	@quarto --version || echo "❌ Quarto not found"
	@echo ""
	@echo "TinyTeX:"
	@quarto list tools | grep -i tinytex || echo "TinyTeX status unknown"
