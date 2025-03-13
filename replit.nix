
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.libnss
    pkgs.libnspr
    pkgs.libdbus
    pkgs.atk
    pkgs.at-spi2-atk
    pkgs.cups
    pkgs.libxcomposite
    pkgs.libxdamage
    pkgs.libxfixes
    pkgs.libgbm
    pkgs.libxcb
    pkgs.libxkbcommon
    pkgs.pango
    pkgs.cairo
    pkgs.alsa-lib
    pkgs.at-spi2-core
    pkgs.nodejs
    # Add playwright-specific package
    pkgs.playwright-driver
  ];
}
